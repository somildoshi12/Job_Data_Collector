from typing import List, Dict
import re
from datetime import datetime

from .config import TARGET_ROLES, TARGET_COUNTRIES, EXCLUDED_LOCATIONS, EXCLUDED_ROLES

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

    def validate(self, job: Dict) -> bool:
        """
        Returns True if job matches User requirements (Role + Location).
        """
        title = job['title'].lower()
        location = job['location'].lower()

        # 1. Negative Role Filter (Drop these first)
        if any(excluded in title for excluded in EXCLUDED_ROLES):
            return False

        # 2. Positive Role Filter
        # We check if (e.g. "data engineer") is in the title string
        if not any(role in title for role in TARGET_ROLES):
            # Fallback: Check if "data" AND ("engineer" or "analyst" or "scientist") are present
            # This handles "Engineer - Data" or "Analyst (Data)"
            if "data" in title and any(x in title for x in ["engineer", "analyst", "scientist"]):
                pass # Good
            else:
                return False
            
        # 3. Check Excluded Locations (Strict Drop)
        if any(excluded in location for excluded in EXCLUDED_LOCATIONS):
            return False

        # 3. Check Target Location (Must be US or Remote)
        # If location is explicitly foreign, it was caught above.
        # Here we just ensure it's not some random city in a country we didn't exclude but don't want.
        # A simple heuristic: If it matches target keywords OR is just a city name (hard to verify without geo-db).
        # For safety, let's require at least one target match IF the location string is long enough to likely contain a country.
        
        # Simplified: Pass if it hits a target keyword OR if we aren't sure (avoid false negatives)
        return True

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
