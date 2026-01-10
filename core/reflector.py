import requests
import uuid

def check_reflection(url):
    marker = f"XSSPECTOR_{uuid.uuid4().hex[:8]}"
    test_url = url.replace("XSS", marker)

    try:
        r = requests.get(test_url, timeout=5)
        if marker in r.text:
            return True
    except:
        pass

    return False
