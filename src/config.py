# Filter Configuration

# Positive Constraints: Title must contain at least one of these
TARGET_ROLES = [
    "data engineer", "data analyst", "data scientist",
    "analytics engineer", "bi analyst", "business intelligence",
    "machine learning", " ml ", "ai engineer", "decision scientist",
    "product analyst", "marketing analyst", "research scientist",
    "etl", "nlp", "computer vision"
]

# Negative Constraints: Title must NOT contain any of these
EXCLUDED_ROLES = [
    "security", "cyber", "hardware", "facility", "facilities",
    "legal", "counsel", "sales", "account executive", "hr",
    "recruiter", "talent", "office", "compliance", "intern", # Unless you want interns
    "manager", "directory", "vp", "head of", "principal", # Seniority filtering (optional)
    "mechanical", "electrical", "civil", "network", "system admin", "support"
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
