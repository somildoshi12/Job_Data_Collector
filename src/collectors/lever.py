import requests
from .base import BaseCollector
from typing import List, Dict

class LeverCollector(BaseCollector):
    def collect(self) -> List[Dict]:
        # URL Logic: https://jobs.lever.co/openai -> openai
        company_slug = self.career_url.rstrip('/').split('/')[-1]
        api_url = f"https://api.lever.co/v0/postings/{company_slug}?mode=json"
        
        print(f"Fetching from Lever API: {api_url}")
        jobs = []
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                for job in data:
                    jobs.append({
                        "company": self.company_name,
                        "title": job.get('text'),
                        "url": job.get('hostedUrl'),
                        "location": job.get('categories', {}).get('location'),
                        "posted_date": str(job.get('createdAt', ''))[:10]
                    })
            else:
                print(f"Lever API Failed: {response.status_code}")
        except Exception as e:
            print(f"Error scraping Lever: {e}")
            
        print(f"Found {len(jobs)} jobs for {self.company_name}")
        return jobs
