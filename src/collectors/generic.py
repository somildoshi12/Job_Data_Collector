from .base import BaseCollector
from typing import List, Dict
from playwright.sync_api import sync_playwright
import time

class GenericCollector(BaseCollector):
    def collect(self) -> List[Dict]:
        print(f"Starting Playwright for: {self.company_name}")
        jobs = []
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()
                page.goto(self.career_url, timeout=60000)
                time.sleep(5)  # Wait for JS to load
                
                # Basic heuristic: Find all 'a' tags that might be jobs
                # This is a fallback; usually custom logic plays here
                links = page.evaluate("""() => {
                    return Array.from(document.querySelectorAll('a')).map(a => ({
                        text: a.innerText,
                        href: a.href
                    }))
                }""")
                
                for link in links:
                    text = link['text'].strip()
                    href = link['href']
                    # Very simple heuristic filtering
                    if len(text) > 4 and ('engineer' in text.lower() or 'analyst' in text.lower() or 'data' in text.lower()):
                        jobs.append({
                            "company": self.company_name,
                            "title": text,
                            "url": href,
                            "location": "Unknown", # Hard to guess generically
                            "posted_date": None
                        })
                
                browser.close()
        except Exception as e:
            print(f"Error scraping {self.company_name}: {e}")
            
        print(f"Found {len(jobs)} potential jobs for {self.company_name}")
        return jobs
