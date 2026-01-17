def verify_execution(response_text, marker):
    proof = []

    if marker in response_text:
        proof.append("Marker Reflected")

    if "<script>" in response_text.lower():
        proof.append("Script Context Detected")

    if f"console.log('{marker}')" in response_text:
        proof.append("JS Execution Context")

    if "onerror=" in response_text.lower():
        proof.append("Event Handler Context")

    return proof if proof else None
