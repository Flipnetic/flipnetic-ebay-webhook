def calculate_vat(
    price: float,
    vat_rate: float = 20.0,
    prices_include_vat: bool = False,
) -> dict:
    """
    Calculate VAT based on whether the supplier price
    already includes VAT.
    """

    if prices_include_vat:
        gross_price = price
        net_price = price / (1 + vat_rate / 100)
        vat_amount = gross_price - net_price
    else:
        net_price = price
        vat_amount = price * (vat_rate / 100)
        gross_price = price + vat_amount

    return {
        "net_price": round(net_price, 2),
        "vat_rate": vat_rate,
        "vat_amount": round(vat_amount, 2),
        "gross_price": round(gross_price, 2),
        "prices_include_vat": prices_include_vat,
    }