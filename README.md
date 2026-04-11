# 🚗💥 Days Since Ohio Crash

**dayssinceohiocrash.com** — Tracking every incident where a car has driven into a building in the Columbus, Ohio metro area.

Satirical. Sourced. Fully static. Costs nothing to run.

---

## How It Works

1. A GitHub Actions cron job runs every morning at 8 AM ET
2. `scripts/scraper.py` searches Google News RSS, Reddit, and Columbus PD/Fire pages for matching incidents
3. New candidates are added to `scripts/candidates.json` and a **pull request is opened for review**
4. You review the PR, approve real incidents into `incidents.json`, delete false positives
5. Merging the PR triggers a Netlify deploy — the counter and feed update automatically

---

## Setup

### 1. Deploy to Netlify

1. Go to [app.netlify.com](https://app.netlify.com) → **Add new site → Import from GitHub**
2. Select this repo (`tonefox/days_since_ohio`)
3. Build settings:
   - **Build command:** *(leave blank — pure static)*
   - **Publish directory:** `.`
4. Click **Deploy**

Netlify auto-deploys on every push to `main`.

### 2. Connect your domain

In Netlify → **Site settings → Domain management**:
- Add custom domain: `dayssinceohiocrash.com`
- Netlify will give you nameservers to set at name.com

### 3. Reddit API credentials (free)

1. Go to [reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
2. Click **Create another app**
   - Type: **script**
   - Name: `OhioCrashBot`
   - Redirect URI: `http://localhost`
3. Copy the **client ID** (under the app name) and **client secret**

### 4. Add secrets to GitHub Actions

In your GitHub repo → **Settings → Secrets and variables → Actions → New repository secret**:

| Secret name | Value |
|---|---|
| `REDDIT_CLIENT_ID` | your Reddit app client ID |
| `REDDIT_CLIENT_SECRET` | your Reddit app client secret |

The scraper runs without Reddit credentials (falls back to Google News + PD/Fire only), but Reddit adds significant signal.

### 5. Generate icons (5 minutes)

1. Go to [favicon.io/emoji-favicons](https://favicon.io/emoji-favicons/)
2. Search for "collision" or use 🚗
3. Download and place in the repo root:
   - `icon-192.png`
   - `icon-512.png`
   - `favicon.ico`

---

## Daily Review Workflow

When the scraper opens a PR:

**Option A — via GitHub (remote):**
1. Open the PR → review `scripts/candidates.json`
2. Edit the file: fill in `location`, `city`, `county`, `building_type`, `status`, `injuries`, `funny_note`
3. Move approved objects into `incidents.json` (assign a sequential `id`)
4. Delete false positives from `candidates.json`
5. Merge the PR

**Option B — locally (faster):**
```bash
git pull
python scripts/approve.py    # interactive CLI walks you through each candidate
python scripts/generate_feed.py
git add incidents.json scripts/candidates.json feed.xml
git commit -m "approve: add incident #N"
git push
```

---

## Adding an Incident Manually

Edit `incidents.json` directly:

```json
{
  "id": 9,
  "date": "2026-04-11",
  "location": "Polaris Pkwy Starbucks",
  "city": "Columbus",
  "county": "Franklin",
  "building_type": "Restaurant",
  "headline": "Car drives into Polaris Starbucks; barista finishes order",
  "funny_note": "The car was not in the mobile order lane. The car is now in the lobby.",
  "source_url": "https://www.nbc4i.com/...",
  "source_name": "NBC4i Columbus",
  "injuries": "none",
  "status": "plywood_phase",
  "reddit_thread": null
}
```

`status` options: `rebuilt` | `plywood_phase` | `condemned`

Then run `python scripts/generate_feed.py` and push.

---

## Project Structure

```
ohio-crash-watch/
├── index.html                  — main page (counter + feed)
├── about.html                  — satire disclaimer + tip submission
├── incidents.json              — approved incidents (source of truth)
├── feed.xml                    — RSS feed (auto-generated)
├── manifest.json               — PWA manifest
├── sw.js                       — service worker (offline support)
├── netlify.toml                — headers, cache rules, Netlify Forms
├── .github/
│   └── workflows/
│       └── daily-scrape.yml    — cron job + PR creation
scripts/
├── scraper.py                  — fetches candidates from 3 sources
├── approve.py                  — interactive CLI for reviewing candidates
├── generate_feed.py            — generates feed.xml from incidents.json
├── candidates.json             — pending review (never deployed)
└── requirements.txt
```

---

## Tech Stack

| Layer | Choice | Cost |
|---|---|---|
| Hosting | Netlify | Free |
| CI/CD | GitHub Actions | Free |
| Reddit API | PRAW + free OAuth app | Free |
| Google News RSS | feedparser | Free |
| Police/Fire scraping | requests + BeautifulSoup | Free |
| Domain | name.com | ~$12/yr |
| **Total** | | **~$12/yr** |

---

## Satire & Legal

This site is **satirical**. All incidents are real and sourced from public reporting. We do not publish personal information about drivers or anyone involved. See [about.html](about.html) for full methodology and inclusion criteria.
