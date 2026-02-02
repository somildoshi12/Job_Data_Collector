import requests
from .base import BaseCollector
from typing import List, Dict

class GreenhouseCollector(BaseCollector):
    def collect(self) -> List[Dict]:
        # URL logic: https://boards.greenhouse.io/anthropic -> anthropic
        board_token = self.career_url.rstrip('/').split('/')[-1]
        api_url = f"https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs?content=true"
        
        print(f"Fetching from Greenhouse API: {api_url}")
        jobs = []
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                for job in data.get('jobs', []):
                    jobs.append({
                        "company": self.company_name,
                        "title": job.get('title'),
                        "url": job.get('absolute_url'),
                        "location": job.get('location', {}).get('name'),
                        "posted_date": job.get('updated_at', '').split('T')[0] # Simple date parsing
                    })
            else:
                print(f"Greenhouse API Failed: {response.status_code}")
        except Exception as e:
            print(f"Error scraping Greenhouse: {e}")
            
        print(f"Found {len(jobs)} jobs for {self.company_name}")
        return jobs
