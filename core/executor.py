import requests

def fire(url, params):
    try:
        response = requests.get(
            url,
            params=params,
            timeout=10,
            allow_redirects=True,
            headers={
                "User-Agent": "XSSPECTOR/1.0 BugBounty Scanner"
            }
        )

        return {
            "text": response.text,
            "final_url": response.url,
            "status": response.status_code,
            "headers": dict(response.headers)
        }

    except Exception as e:
        return None
