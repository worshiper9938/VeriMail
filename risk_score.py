# risk_score.py

def calculate_risk(details: dict):
    score = 100

    if not details.get("has_mx_records", True):
        score -= 50

    if details.get("is_disposable", False):
        score -= 40

    if details.get("suggested_domain") is not None:
        score -= 25

    if details.get("domain_fresh", False):  # optional WHOIS später
        score -= 20

    return max(score, 0)
