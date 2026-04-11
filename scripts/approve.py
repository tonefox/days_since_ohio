#!/usr/bin/env python3
"""
Days Since Ohio Crash — Candidate Review CLI
Interactively approve or reject scraper candidates.
Approved incidents are added to incidents.json and removed from candidates.json.

Usage:
    python scripts/approve.py

Controls:
    a  — Approve (will prompt for missing fields)
    s  — Skip (leave in candidates for later)
    d  — Delete / reject (removes from candidates permanently)
    q  — Quit and save
"""

import json
import sys
from pathlib import Path
from datetime import datetime

SCRIPT_DIR      = Path(__file__).parent
REPO_ROOT       = SCRIPT_DIR.parent
INCIDENTS_FILE  = REPO_ROOT / "incidents.json"
CANDIDATES_FILE = SCRIPT_DIR / "candidates.json"

BUILDING_TYPES = [
    "Restaurant", "Retail", "Pharmacy", "Grocery", "Auto Parts Store",
    "Gas Station", "Bank", "Medical", "Office", "Other",
]
STATUSES = ["rebuilt", "plywood_phase", "condemned", "unknown"]
INJURIES = ["none", "minor", "serious", "fatal", "unknown"]

RESET  = "\033[0m"
BOLD   = "\033[1m"
CYAN   = "\033[96m"
GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
DIM    = "\033[2m"


def load_json(path, default):
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return default


def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=str)


def pick(prompt, options, default=None):
    print(f"\n{DIM}{prompt}{RESET}")
    for i, o in enumerate(options, 1):
        marker = " (default)" if o == default else ""
        print(f"  {DIM}{i}.{RESET} {o}{marker}")
    while True:
        raw = input(f"  Choice [1-{len(options)}]: ").strip()
        if not raw and default:
            return default
        try:
            idx = int(raw) - 1
            if 0 <= idx < len(options):
                return options[idx]
        except ValueError:
            pass
        print(f"  {RED}Enter a number 1–{len(options)}.{RESET}")


def ask(prompt, default=""):
    val = input(f"{DIM}{prompt}{RESET} [{default}]: ").strip()
    return val if val else default


def next_id(incidents):
    if not incidents:
        return 1
    return max(i["id"] for i in incidents) + 1


def approve_candidate(candidate, incidents):
    """Prompt user to fill in required fields, then append to incidents."""
    print(f"\n{BOLD}{GREEN}Approving...{RESET}")

    loc   = ask("Location (e.g. 'Sawmill Rd Chipotle')", candidate.get("location", ""))
    city  = ask("City", candidate.get("city", "Columbus"))
    county = ask("County", candidate.get("county", "Franklin"))
    btype = pick("Building type", BUILDING_TYPES, candidate.get("building_type", ""))
    status = pick("Building status", STATUSES, candidate.get("status", "rebuilt"))
    inj   = pick("Injuries", INJURIES, candidate.get("injuries", "none"))
    funny = ask("Funny note (optional)", candidate.get("funny_note", ""))
    reddit = ask("Reddit thread URL (optional, press enter to skip)", candidate.get("reddit_thread") or "")

    incident = {
        "id":           next_id(incidents),
        "date":         candidate["date"],
        "location":     loc,
        "city":         city,
        "county":       county,
        "building_type": btype,
        "headline":     candidate["title"],
        "funny_note":   funny,
        "source_url":   candidate["source_url"],
        "source_name":  candidate["source_name"],
        "injuries":     inj,
        "status":       status,
        "reddit_thread": reddit or None,
    }

    incidents.append(incident)
    print(f"\n{GREEN}✓ Added as incident #{incident['id']}{RESET}")
    return incident


def main():
    candidates = load_json(CANDIDATES_FILE, [])
    incidents  = load_json(INCIDENTS_FILE, [])

    if not candidates:
        print(f"{YELLOW}No candidates to review. Run scraper.py first.{RESET}")
        sys.exit(0)

    print(f"\n{BOLD}{'─' * 60}{RESET}")
    print(f"{BOLD}Days Since Ohio Crash — Candidate Review{RESET}")
    print(f"{DIM}{len(candidates)} candidate(s) pending · {len(incidents)} approved so far{RESET}")
    print(f"{BOLD}{'─' * 60}{RESET}")
    print(f"  {GREEN}a{RESET} = approve  {YELLOW}s{RESET} = skip  {RED}d{RESET} = delete  {CYAN}q{RESET} = quit\n")

    remaining = []
    approved_count = 0
    deleted_count  = 0

    for i, c in enumerate(candidates, 1):
        print(f"\n{BOLD}[{i}/{len(candidates)}] {CYAN}{c['title']}{RESET}")
        print(f"  {DIM}Date:{RESET}   {c['date']}")
        print(f"  {DIM}Source:{RESET} {c['source_name']}")
        print(f"  {DIM}URL:{RESET}    {c['source_url'][:80]}{'…' if len(c['source_url']) > 80 else ''}")

        while True:
            action = input(f"\n  Action [{GREEN}a{RESET}/{YELLOW}s{RESET}/{RED}d{RESET}/{CYAN}q{RESET}]: ").strip().lower()
            if action == "q":
                print(f"\n{CYAN}Quitting early — saving progress.{RESET}")
                remaining.extend(candidates[i - 1:])  # keep current + rest
                # Remove already-processed ones from remaining
                remaining = [c for c in candidates[i:]]
                # Add back skipped ones
                break
            elif action == "a":
                approve_candidate(c, incidents)
                approved_count += 1
                break
            elif action == "s":
                remaining.append(c)
                print(f"  {YELLOW}Skipped.{RESET}")
                break
            elif action == "d":
                deleted_count += 1
                print(f"  {RED}Deleted.{RESET}")
                break
            else:
                print(f"  {RED}Press a, s, d, or q.{RESET}")

        if action == "q":
            break

    # Save
    save_json(INCIDENTS_FILE, sorted(incidents, key=lambda x: x["date"], reverse=True))
    save_json(CANDIDATES_FILE, remaining)

    print(f"\n{BOLD}{'─' * 60}")
    print(f"Done. {GREEN}+{approved_count} approved{RESET}  {RED}-{deleted_count} deleted{RESET}  {YELLOW}{len(remaining)} remaining{RESET}")
    print(f"{BOLD}{'─' * 60}{RESET}\n")

    if approved_count > 0:
        print(f"Now run: {CYAN}python scripts/generate_feed.py{RESET} to update feed.xml")
        print(f"Then commit and push to deploy.\n")


if __name__ == "__main__":
    main()
