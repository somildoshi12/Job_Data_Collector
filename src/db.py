from supabase import create_client, Client
import os

class Database:
    def __init__(self):
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")
        if not url or not key:
            raise ValueError("Missing Supabase Environment Variables")
        self.supabase: Client = create_client(url, key)

    def get_companies(self):
        """Fetch all companies to scrape."""
        try:
            response = self.supabase.table("companies").select("*").execute()
            return response.data
        except Exception as e:
            print(f"Error fetching companies: {e}")
            return []

    def save_jobs(self, jobs):
        """Upsert jobs to database."""
        if not jobs:
            return
        
        try:
            # Using 'upsert' to update existing jobs (handle duplicates by URL)
            # Assuming 'url' is a unique constraint in DB as per setup guide
            response = self.supabase.table("jobs").upsert(jobs, on_conflict="url").execute()
            print(f"Saved {len(jobs)} jobs to Supabase.")
        except Exception as e:
            print(f"Error saving jobs: {e}")
