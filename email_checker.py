# email_checker.py

import dns.resolver
from typo_check import suggest_domain
from risk_score import calculate_risk
from disposable_email_domains import blocklist

CUSTOM_DISPOSABLE = {
    "tempmail.plus",
    "fakeinbox.com",
    "emailondeck.com",
    "dropmail.me",
    "trashmail.ws",
    "spam4.me",
    "dispostable.com",
    "getairmail.com",
    "mytrashmail.com",
    "mintemail.com",
    "spambog.com",
    "anonymbox.com",
    "easytrashmail.com",
    "noclickemail.com",
    "nowmymail.com",
    "mailhazard.com",
    "youmailr.com",
    "incognitomail.org",
    "spamgourmet.com",
}


def check_email(email):
    domain = email.split('@')[1]

    # MX Record Check
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        has_mx = len(mx_records) > 0
    except:
        has_mx = False

    # Disposable Check
    is_disposable = domain in blocklist or domain in CUSTOM_DISPOSABLE

    # Typo-Vorschlag
    suggested = suggest_domain(domain)

    # Ergebnis zusammenbauen
    result = {
        "is_valid_syntax": True,
        "is_disposable": is_disposable,
        "has_mx_records": has_mx,
        "suggested_domain": suggested,
    }

    # Risk Score berechnen
    result["risk_score"] = calculate_risk(result)

    return result
