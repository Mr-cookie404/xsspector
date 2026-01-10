import urllib.parse

def normalize_url(url):
    try:
        parsed = urllib.parse.urlparse(url.strip())
        return parsed
    except Exception:
        return None
