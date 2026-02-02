from typing import List, Dict
import re
from datetime import datetime

class JobNormalizer:
    def normalize(self, job_raw: Dict) -> Dict:
        """
        Standardizes job data to match the database schema.
        """
        return {
            "title": self._clean_text(job_raw.get("title", "")),
            # "company": job_raw.get("company", ""), # Redundant, handled by company_id
            "url": job_raw.get("url", ""),
            "location": self._clean_text(job_raw.get("location", "Unknown")),
            "posted_date": self._parse_date(job_raw.get("posted_date")),
            "is_active": True
        }

    def _clean_text(self, text: str) -> str:
        if not text:
            return ""
        # Remove extra whitespace
        return re.sub(r'\s+', ' ', text).strip()

    def _parse_date(self, date_str: str) -> str:
        # TODO: Implement robust date parsing if needed
        # For now return None if invalid or current date if missing
        if not date_str:
            return None
        return date_str
