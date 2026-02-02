# User Setup Guide

## 1. Install Node.js
The frontend requires Node.js.
- **Mac**: `brew install node`
- **Verify**: Run `node -v` in your terminal.

## 2. Supabase Setup (Database)
1. Go to [database.new](https://database.new) and create a free project.
2. Open the **SQL Editor** in the side menu.
3. Copy and Run this SQL:
   ```sql
   create table companies (
       id bigint primary key generated always as identity,
       name text not null,
       career_url text not null,
       created_at timestamptz default now()
   );

   create table jobs (
       id bigint primary key generated always as identity,
       company_id bigint references companies(id),
       title text not null,
       url text not null unique,
       location text,
       posted_date date,
       is_active boolean default true,
       created_at timestamptz default now()
   );
   
   -- Insert a test company
   insert into companies (name, career_url) 
   values ('Test Company', 'https://boards.greenhouse.io/test');
   ```

## 3. Environment Variables
1. Go to **Project Settings** -> **API** in Supabase.
2. Copy **Project URL** and **service_role secret** (NOT the anon key).
3. Create a file named `.env` in this folder:
   ```env
   SUPABASE_URL=your_project_url_here
   SUPABASE_KEY=your_service_role_secret_here
   ```
