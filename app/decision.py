def get_decision(score: int) -> str:
    if score >= 75:
        return "BUY"
    elif score >= 50:
        return "REVIEW"
    else:
        return "PASS"