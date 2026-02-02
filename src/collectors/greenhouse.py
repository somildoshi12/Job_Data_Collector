import requests
from .base import BaseCollector
from typing import List, Dict

class GreenhouseCollector(BaseCollector):
    def collect(self) -> List[Dict]:
        # Example: https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs
        # For now, we'll implement a basic HTML parser or API fetcher
        print(f"Collecting from Greenhouse: {self.company_name}")
        return []
