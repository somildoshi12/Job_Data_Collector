# Job Data Collector

A self-hosted, automated system to collect job postings from company career pages.

## Architecture
- **Backend**: Supabase (Postgres)
- **Scraper**: Python + Playwright (Runs on GitHub Actions)
- **Frontend**: React + Vite (Hosted on GitHub Pages)

## Setup
### Python
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install
```

### Frontend
```bash
cd web
npm install
npm run dev
```
