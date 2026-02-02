import os
import argparse
from dotenv import load_dotenv
from .db import Database
from .normalizer import JobNormalizer
from .collectors.greenhouse import GreenhouseCollector
from .collectors.lever import LeverCollector
from .collectors.generic import GenericCollector

# Load environment variables
load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="Job Data Collector")
    parser.add_argument("--manual", action="store_true", help="Run manually triggered scrape")
    args = parser.parse_args()
    
    print("Starting Job Collector...")
    
    try:
        db = Database()
        companies = db.get_companies()
        print(f"Found {len(companies)} companies to process.")
        
        normalizer = JobNormalizer()
        
        for company in companies:
            name = company.get('name')
            url = company.get('career_url')
            cid = company.get('id')
            
            # --- AUTO DISCOVERY LOGIC ---
            if url == "AUTO_DISCOVER" or not url:
                print(f"🕵️‍♂️ finding career page for: {name}...")
                try:
                    from googlesearch import search
                    # Search for "Company Name careers"
                    query = f"{name} careers jobs"
                    results = list(search(query, num_results=1))
                    if results:
                        url = results[0]
                        print(f"✅ Found URL: {url}")
                        # Update DB so we don't search again
                        db.supabase.table("companies").update({"career_url": url}).eq("id", cid).execute()
                    else:
                        print(f"❌ Could not find URL for {name}")
                        continue # Skip scraping
                except Exception as e:
                    print(f"Error searching for URL: {e}")
                    continue # Skip scraping
            
            if url == "AUTO_DISCOVER" or not url:
                print(f"⚠️ Skipping {name} (No URL)")
                continue
            # ---------------------------
            
            # Select Collector
            collector = None
            if 'greenhouse' in url:
                collector = GreenhouseCollector(name, url)
            elif 'lever' in url:
                collector = LeverCollector(name, url)
            else:
                collector = GenericCollector(name, url)
                
            raw_jobs = collector.collect()
            
            # Normalize and Prepare
            clean_jobs = []
            for job in raw_jobs:
                normalized_job = normalizer.normalize(job)
                
                # Apply Filters
                if normalizer.validate(normalized_job):
                    normalized_job['company_id'] = cid # Link foreign key
                    clean_jobs.append(normalized_job)
                
            # Save
            if clean_jobs:
                db.save_jobs(clean_jobs)
                
    except Exception as e:
        print(f"Fatal Error: {e}")
        print("Tip: Check if .env file exists and has SUPABASE_URL and SUPABASE_KEY")
    
if __name__ == "__main__":
    main()
