import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

def clean_db():
    supabase_url = os.environ.get("SUPABASE_URL")
    supabase_key = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(supabase_url, supabase_key)
    
    # Delete all jobs to start fresh
    print("Cleaning all jobs from database...")
    supabase.table("jobs").delete().neq("id", 0).execute() # Delete where id != 0 (all)
    print("Done.")

if __name__ == "__main__":
    clean_db()
