def calculate_profit(
    buy_price: float,
    sale_price: float,
    ebay_fee: float,
    postage: float,
) -> dict:
    profit = sale_price - buy_price - ebay_fee - postage

    if buy_price > 0:
        roi = (profit / buy_price) * 100
    else:
        roi = 0.0

    return {
        "profit": round(profit, 2),
        "roi": round(roi, 2),
    }