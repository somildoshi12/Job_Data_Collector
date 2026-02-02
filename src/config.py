# Filter Configuration

# Only keep jobs if title contains at least one of these (case-insensitive)
TARGET_ROLES = [
    "data", "analyst", "engineer", "scientist", 
    "machine learning", "ai", "business intelligence", "etl",
    "python", "sql"
]

# Only keep jobs if location matches one of these (case-insensitive)
# If location is empty/unknown, we might keep it or drop it based on preference.
# For now, we will be permissive with "Remote" but strict with countries.
TARGET_COUNTRIES = [
    "united states", "usa", "us", "remote", "home based", "anywhere"
]

# If location contains these, DROP IT (e.g. UK, Canada if you only want US)
EXCLUDED_LOCATIONS = [
    "united kingdom", "uk", "london", "canada", "toronto", "vancouver",
    "germany", "berlin", "france", "paris", "india", "bangalore", "australia",
    "emea", "apac"
]
