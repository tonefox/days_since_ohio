#!/usr/bin/env python3
"""
Days Since Ohio Crash — Daily Scraper
Fetches candidate incidents from Google News RSS, Reddit, and Columbus PD/Fire.
Writes new (unseen) candidates to candidates.json for human review.

Usage:
    pip install -r requirements.txt
    export REDDIT_CLIENT_ID=...
    export REDDIT_CLIENT_SECRET=...
    python scraper.py
"""

import os
import json
import hashlib
import logging
from datetime import datetime, timezone, timedelta
from pathlib import Path

import feedparser
import praw
import requests
from bs4 import BeautifulSoup
from dateutil import parser as dateparser

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger(__name__)

# ── Paths ────────────────────────────────────────────────────────────────────
SCRIPT_DIR      = Path(__file__).parent
REPO_ROOT       = SCRIPT_DIR.parent
INCIDENTS_FILE  = REPO_ROOT / "incidents.json"
CANDIDATES_FILE = SCRIPT_DIR / "candidates.json"
SEEN_FILE       = SCRIPT_DIR / ".seen_urls.json"
STATUS_FILE     = REPO_ROOT / "api-status.json"

# ── Keyword filters ───────────────────────────────────────────────────────────
VEHICLE_TERMS = [
    "car", "vehicle", "suv", "truck", "pickup", "minivan", "sedan",
    "van", "automobile", "driver", "motorist",
]
IMPACT_TERMS = [
    "drove into", "crashed into", "plowed into", "through wall",
    "into building", "into storefront", "through storefront",
    "into store", "into restaurant", "through the wall", "smashed into",
    "slammed into", "barreled into", "careened into",
    "into home", "into house", "into residence", "into garage",
    "through the front", "through a home", "through a house",
]
OHIO_LOCATIONS = [
    "Columbus", "Dublin", "Westerville", "Gahanna", "Hilliard",
    "Grove City", "Reynoldsburg", "Pickerington", "Worthington",
    "Bexley", "Upper Arlington", "New Albany", "Groveport",
    "Delaware", "Newark", "Lancaster", "Pataskala", "Obetz", "Ohio",
    "Franklin County", "Delaware County", "Licking County", "Fairfield County",
]

# ── Google News RSS queries ───────────────────────────────────────────────────
GNEWS_QUERIES = [
    "car crashed into building Columbus Ohio",
    "vehicle drove into storefront Ohio",
    "car plowed into building Columbus",
    "car through wall Ohio",
    "vehicle into store Columbus Ohio",
]
GNEWS_BASE = "https://news.google.com/rss/search?q={q}&hl=en-US&gl=US&ceid=US:en"

# ── Reddit config ─────────────────────────────────────────────────────────────
REDDIT_SUBREDDITS = ["Columbus", "Ohio", "columbusoh"]
REDDIT_SEARCH_QUERY = (
    '"drove into" OR "crashed into" OR "plowed into" OR "through wall" '
    'OR "into building" OR "into storefront" building'
)

# ── Columbus PD / Fire pages ──────────────────────────────────────────────────
PUBLIC_SAFETY_SOURCES = [
    {
        "name": "Columbus Division of Police",
        "url": "https://www.columbus.gov/police/",
        "selector": "a",  # scrape all links, filter by keyword
    },
    {
        "name": "Columbus Fire / EMS",
        "url": "https://www.columbusfire.org/",
        "selector": "a",
    },
]

# ─────────────────────────────────────────────────────────────────────────────

def load_json(path: Path, default):
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return default

def save_json(path: Path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=str)

def url_hash(url: str) -> str:
    return hashlib.sha256(url.encode()).hexdigest()[:16]

def matches_filters(text: str) -> bool:
    """Return True if text contains vehicle + impact + Ohio location keywords."""
    lower = text.lower()
    has_vehicle = any(t in lower for t in VEHICLE_TERMS)
    has_impact  = any(t in lower for t in IMPACT_TERMS)
    has_ohio    = any(loc.lower() in lower for loc in OHIO_LOCATIONS)
    return has_vehicle and has_impact and has_ohio

def make_candidate(title: str, url: str, source_name: str, pub_date=None) -> dict:
    return {
        "title":       title.strip(),
        "source_url":  url.strip(),
        "source_name": source_name,
        "date":        (pub_date or datetime.now(timezone.utc)).strftime("%Y-%m-%d"),
        "url_hash":    url_hash(url),
        "scraped_at":  datetime.now(timezone.utc).isoformat(),
        # Fields for human review to fill in:
        "location":       "",
        "city":           "",
        "county":         "",
        "building_type":  "",
        "funny_note":     "",
        "injuries":       "",
        "status":         "rebuilt",
        "reddit_thread":  None,
    }

# ── Source: Google News RSS ───────────────────────────────────────────────────
def fetch_google_news(seen_hashes: set) -> tuple[list[dict], dict]:
    candidates = []
    total_checked = 0
    last_error = None
    for query in GNEWS_QUERIES:
        url = GNEWS_BASE.format(q=requests.utils.quote(query))
        log.info(f"[Google News] {query}")
        try:
            feed = feedparser.parse(url)
            total_checked += len(feed.entries)
            for entry in feed.entries:
                link  = entry.get("link", "")
                title = entry.get("title", "")
                h     = url_hash(link)
                if h in seen_hashes:
                    continue
                combined = f"{title} {entry.get('summary', '')}"
                if not matches_filters(combined):
                    continue
                try:
                    pub = dateparser.parse(entry.get("published", ""))
                except Exception:
                    pub = None
                candidates.append(make_candidate(title, link, "Google News / Local", pub))
                seen_hashes.add(h)
                log.info(f"  ✓ {title[:80]}")
        except Exception as e:
            last_error = str(e)
            log.warning(f"  Google News error: {e}")

    status = {
        "label":        "Google News RSS",
        "requires_setup": False,
        "status":       "error" if last_error and not candidates else "ok",
        "note":         last_error or f"No auth required. {total_checked} articles scanned.",
        "new_candidates": len(candidates),
        "last_checked": datetime.now(timezone.utc).isoformat(),
    }
    return candidates, status

# ── Source: Reddit ────────────────────────────────────────────────────────────
def fetch_reddit(seen_hashes: set) -> tuple[list[dict], dict]:
    client_id     = os.environ.get("REDDIT_CLIENT_ID", "")
    client_secret = os.environ.get("REDDIT_CLIENT_SECRET", "")

    if not client_id or not client_secret:
        log.warning("[Reddit] Skipping — REDDIT_CLIENT_ID / REDDIT_CLIENT_SECRET not set")
        status = {
            "label":          "Reddit API (PRAW)",
            "requires_setup": True,
            "status":         "not_configured",
            "note":           "Add REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET to GitHub Secrets. Free at reddit.com/prefs/apps.",
            "setup_url":      "https://www.reddit.com/prefs/apps",
            "new_candidates": 0,
            "last_checked":   datetime.now(timezone.utc).isoformat(),
        }
        return [], status

    candidates = []
    last_error = None
    try:
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent="OhioCrashBot/1.0 (dayssinceohiocrash.com)",
        )
        for sub_name in REDDIT_SUBREDDITS:
            log.info(f"[Reddit] r/{sub_name}")
            sub = reddit.subreddit(sub_name)
            for post in sub.search(REDDIT_SEARCH_QUERY, sort="new", time_filter="week", limit=50):
                link  = f"https://reddit.com{post.permalink}"
                title = post.title
                h     = url_hash(link)
                if h in seen_hashes:
                    continue
                combined = f"{title} {post.selftext[:500]}"
                if not matches_filters(combined):
                    continue
                pub = datetime.fromtimestamp(post.created_utc, tz=timezone.utc)
                c = make_candidate(title, link, f"Reddit r/{sub_name}", pub)
                c["reddit_thread"] = link
                candidates.append(c)
                seen_hashes.add(h)
                log.info(f"  ✓ {title[:80]}")
    except Exception as e:
        last_error = str(e)
        log.warning(f"[Reddit] Error: {e}")

    status = {
        "label":          "Reddit API (PRAW)",
        "requires_setup": True,
        "status":         "error" if last_error else "ok",
        "note":           last_error or f"Monitoring: {', '.join('r/'+s for s in REDDIT_SUBREDDITS)}",
        "new_candidates": len(candidates),
        "last_checked":   datetime.now(timezone.utc).isoformat(),
    }
    return candidates, status

# ── Source: Columbus PD / Fire ────────────────────────────────────────────────
def fetch_public_safety(seen_hashes: set) -> tuple[list[dict], dict]:
    candidates = []
    source_statuses = []
    headers = {"User-Agent": "OhioCrashBot/1.0 (dayssinceohiocrash.com)"}

    for source in PUBLIC_SAFETY_SOURCES:
        log.info(f"[Public Safety] {source['name']}")
        try:
            resp = requests.get(source["url"], headers=headers, timeout=15)
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, "html.parser")
            found = 0
            for tag in soup.select(source["selector"]):
                text = tag.get_text(strip=True)
                href = tag.get("href", "")
                if not href or not text:
                    continue
                if not href.startswith("http"):
                    from urllib.parse import urljoin
                    href = urljoin(source["url"], href)
                h = url_hash(href)
                if h in seen_hashes:
                    continue
                if not matches_filters(text):
                    continue
                candidates.append(make_candidate(text, href, source["name"]))
                seen_hashes.add(h)
                found += 1
                log.info(f"  ✓ {text[:80]}")
            source_statuses.append({"name": source["name"], "status": "ok", "found": found})
        except Exception as e:
            log.warning(f"  Error scraping {source['name']}: {e}")
            source_statuses.append({"name": source["name"], "status": "error", "error": str(e)})

    overall = "ok" if all(s["status"] == "ok" for s in source_statuses) else "partial"
    status = {
        "label":          "Columbus PD / Fire (public pages)",
        "requires_setup": False,
        "status":         overall,
        "note":           "No auth required. Scrapes public press release pages.",
        "sources":        source_statuses,
        "new_candidates": len(candidates),
        "last_checked":   datetime.now(timezone.utc).isoformat(),
    }
    return candidates, status

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    # Load existing seen URL hashes so we don't re-surface old results
    seen_hashes = set(load_json(SEEN_FILE, []))

    # Also mark all already-approved incident URLs as seen
    approved = load_json(INCIDENTS_FILE, [])
    for inc in approved:
        seen_hashes.add(url_hash(inc.get("source_url", "")))

    # Fetch from all sources
    new_candidates = []
    source_statuses = []

    gnews_results, gnews_status = fetch_google_news(seen_hashes)
    new_candidates.extend(gnews_results)
    source_statuses.append(gnews_status)

    reddit_results, reddit_status = fetch_reddit(seen_hashes)
    new_candidates.extend(reddit_results)
    source_statuses.append(reddit_status)

    safety_results, safety_status = fetch_public_safety(seen_hashes)
    new_candidates.extend(safety_results)
    source_statuses.append(safety_status)

    # Merge with existing candidates (don't overwrite what's pending review)
    existing = load_json(CANDIDATES_FILE, [])
    existing_hashes = {c["url_hash"] for c in existing}
    truly_new = [c for c in new_candidates if c["url_hash"] not in existing_hashes]

    merged = existing + truly_new
    save_json(CANDIDATES_FILE, merged)

    # Persist updated seen hashes
    save_json(SEEN_FILE, list(seen_hashes))

    # Write api-status.json so admin.html can display live source health
    api_status = {
        "last_run":   datetime.now(timezone.utc).isoformat(),
        "new_total":  len(truly_new),
        "sources":    source_statuses,
    }
    save_json(STATUS_FILE, api_status)
    log.info(f"✓ api-status.json updated.")

    log.info(f"\nDone. {len(truly_new)} new candidate(s) added. {len(merged)} total pending review.")
    log.info(f"Edit {CANDIDATES_FILE} to review, then move approved items to {INCIDENTS_FILE}.")

if __name__ == "__main__":
    main()
