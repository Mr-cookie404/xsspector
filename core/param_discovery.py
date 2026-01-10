import urllib.parse
import re

SUSPICIOUS_PARAM_PATTERNS = [
    r"q|s|search|query|keyword",
    r"redirect|url|next|return|callback",
    r"id|item|view|page|lang",
    r"utm_.*",
    r"ref|source|data"
]

def extract_parameters(parsed_url):
    discovered = []

    # Standard query params
    params = urllib.parse.parse_qs(parsed_url.query, keep_blank_values=True)

    for param, values in params.items():
        discovered.append({
            "name": param,
            "value": values[0] if values else "",
            "type": "query"
        })

    # Detect encoded params inside values
    for value in params.values():
        for v in value:
            if "=" in v and "&" in v:
                nested = urllib.parse.parse_qs(v)
                for n in nested:
                    discovered.append({
                        "name": n,
                        "value": nested[n][0],
                        "type": "nested"
                    })

    return discovered
