import uuid

def generate_payload():
    marker = f"XSSPECTOR_{uuid.uuid4().hex[:8]}"

    payload = f"'><script>console.log('{marker}')</script>"

    return payload, marker
