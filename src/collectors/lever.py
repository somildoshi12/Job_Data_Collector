import requests
from .base import BaseCollector
from typing import List, Dict

class LeverCollector(BaseCollector):
    def collect(self) -> List[Dict]:
        # Example: https://api.lever.co/v0/postings/{company}
        print(f"Collecting from Lever: {self.company_name}")
        return []
