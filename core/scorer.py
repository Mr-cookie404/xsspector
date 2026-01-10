def calculate_score(factors):
    score = 0
    for f in factors:
        score += f
    return "HIGH" if score >= 8 else "MEDIUM" if score >= 4 else "LOW"
