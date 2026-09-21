def calculate_score(
    profit: float,
    roi: float,
    sales_count: int,
    competition: int,
) -> int:

    score = 0

    # Profit
    if profit >= 10:
        score += 30
    elif profit >= 5:
        score += 20
    elif profit >= 2:
        score += 10

    # ROI
    if roi >= 100:
        score += 25
    elif roi >= 50:
        score += 20
    elif roi >= 30:
        score += 15
    elif roi >= 20:
        score += 10

    # Sales activity
    if sales_count >= 50:
        score += 25
    elif sales_count >= 20:
        score += 20
    elif sales_count >= 10:
        score += 15
    elif sales_count >= 5:
        score += 10
    elif sales_count >= 2:
        score += 5

    # Competition
    if competition <= 5:
        score += 20
    elif competition <= 10:
        score += 15
    elif competition <= 20:
        score += 10
    elif competition <= 50:
        score += 5

    return min(score, 100)