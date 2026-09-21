def lookup_ean(ean: str) -> dict:
    """
    Temporary EAN lookup for development testing.
    """

    ean = ean.strip()

    if not ean:
        return {
            "found": False,
            "error": "No EAN was entered.",
        }

    if ean == "3614228412537":
        return {
            "found": True,
            "ean": ean,
            "name": "Bourjois Twist Extreme Fiber Mascara - 024 Black",
            "brand": "Bourjois",
        }

    return {
        "found": False,
        "ean": ean,
        "error": "Product not found.",
    }