import os
import argparse
from typing import Optional
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

def add_company(name: str, url: str):
    supabase_url = os.environ.get("SUPABASE_URL")
    supabase_key = os.environ.get("SUPABASE_KEY")
    
    if not supabase_url or not supabase_key:
        print("Error: Missing SUPABASE_URL or SUPABASE_KEY in .env")
        return

    supabase: Client = create_client(supabase_url, supabase_key)
    
    try:
        data = {"name": name, "career_url": url}
        response = supabase.table("companies").insert(data).execute()
        print(f"Successfully added company: {name}")
    except Exception as e:
        print(f"Error adding company: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True, help="Company Name")
    parser.add_argument("--url", required=True, help="Career Page URL")
    args = parser.parse_args()
    
    add_company(args.name, args.url)
