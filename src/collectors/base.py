from abc import ABC, abstractmethod
from typing import List, Dict, Optional

class BaseCollector(ABC):
    def __init__(self, company_name: str, career_url: str):
        self.company_name = company_name
        self.career_url = career_url

    @abstractmethod
    def collect(self) -> List[Dict]:
        """
        Scrape the career page and return a list of jobs.
        Each job should match the standard schema:
        {
            "company": str,
            "title": str,
            "url": str,
            "location": str,
            "posted_date": str (optional)
        }
        """
        pass
    
    def normalize(self, jobs: List[Dict]) -> List[Dict]:
        """Optional: Normalize data if needed here"""
        return jobs
