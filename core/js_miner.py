import re

JS_PARAM_PATTERNS = [
    r'URLSearchParams\([^)]+\)\.get\(["\'](.*?)["\']\)',
    r'location\.search.*?[\'"](\w+)[\'"]',
    r'location\.hash.*?[\'"](\w+)[\'"]',
    r'document\.referrer',
    r'window\.name'
]

def extract_js_params(js_content):
    found = set()
    for pattern in JS_PARAM_PATTERNS:
        matches = re.findall(pattern, js_content)
        for m in matches:
            if isinstance(m, str) and len(m) > 1:
                found.add(m)
    return list(found)
