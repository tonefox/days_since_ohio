#!/usr/bin/env python3
"""
Days Since Ohio Crash — RSS Feed Generator
Reads incidents.json and writes /feed.xml to the repo root.

Run manually or as part of GitHub Actions after incidents.json changes:
    python scripts/generate_feed.py
"""

import json
from pathlib import Path
from datetime import datetime, timezone
from xml.sax.saxutils import escape

SCRIPT_DIR     = Path(__file__).parent
REPO_ROOT      = SCRIPT_DIR.parent
INCIDENTS_FILE = REPO_ROOT / "incidents.json"
FEED_FILE      = REPO_ROOT / "feed.xml"

SITE_URL   = "https://dayssinceohiocrash.com"
SITE_TITLE = "Days Since Ohio Crash"
SITE_DESC  = (
    "Tracking every incident where a car has driven into a building "
    "in the Columbus, Ohio metro area. Sourced. Verified. Satirical."
)


def rfc822(date_str: str) -> str:
    """Convert YYYY-MM-DD to RFC 822 format for RSS."""
    dt = datetime.fromisoformat(date_str + "T12:00:00+00:00")
    return dt.strftime("%a, %d %b %Y %H:%M:%S +0000")


def build_item(incident: dict) -> str:
    title   = escape(incident["headline"])
    link    = escape(incident["source_url"])
    desc    = escape(
        incident["headline"]
        + (f' — {incident["funny_note"]}' if incident.get("funny_note") else "")
        + f' | {incident["location"]}, {incident["city"]} OH'
        + f' | via {incident["source_name"]}'
    )
    pub     = rfc822(incident["date"])
    guid    = escape(f'{SITE_URL}/incident/{incident["id"]}')
    cat     = escape(incident.get("building_type", ""))

    return f"""    <item>
      <title>{title}</title>
      <link>{link}</link>
      <description>{desc}</description>
      <pubDate>{pub}</pubDate>
      <guid isPermaLink="false">{guid}</guid>
      <category>{cat}</category>
    </item>"""


def main():
    with open(INCIDENTS_FILE) as f:
        incidents = json.load(f)

    # Sort by date descending
    incidents.sort(key=lambda i: i["date"], reverse=True)

    now    = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")
    items  = "\n".join(build_item(i) for i in incidents[:50])  # latest 50

    # Days since last incident
    days   = (datetime.now(timezone.utc).date() -
              datetime.fromisoformat(incidents[0]["date"]).date()).days if incidents else "?"

    feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{escape(SITE_TITLE)}</title>
    <link>{SITE_URL}</link>
    <description>{escape(SITE_DESC)} Currently: {days} day(s) since last incident.</description>
    <language>en-us</language>
    <lastBuildDate>{now}</lastBuildDate>
    <atom:link href="{SITE_URL}/feed.xml" rel="self" type="application/rss+xml"/>
    <image>
      <url>{SITE_URL}/icon-192.png</url>
      <title>{escape(SITE_TITLE)}</title>
      <link>{SITE_URL}</link>
    </image>
{items}
  </channel>
</rss>
"""

    with open(FEED_FILE, "w") as f:
        f.write(feed)

    print(f"✓ feed.xml written with {len(incidents)} incident(s). Days since last: {days}")


if __name__ == "__main__":
    main()
