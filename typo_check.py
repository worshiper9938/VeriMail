# typo_check.py

from difflib import get_close_matches

# Liste gängiger Domains – erweiterbar
KNOWN_DOMAINS = [
    "gmail.com", "gmx.de", "web.de", "yahoo.com", "hotmail.com",
    "outlook.com", "t-online.de", "icloud.com", "protonmail.com"
]

def suggest_domain(domain):
    matches = get_close_matches(domain, KNOWN_DOMAINS, n=1, cutoff=0.8)
    if matches and matches[0] != domain:
        return matches[0]
    return None
