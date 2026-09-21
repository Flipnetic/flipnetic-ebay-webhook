import re

import requests


def get_supplier_product(url: str) -> dict:
    """
    Download a supplier product page.

    This only requests the supplied product URL.
    """

    try:
        response = requests.get(
            url,
            timeout=15,
            headers={
                "User-Agent": "Flipnetic/0.1",
            },
        )

        response.raise_for_status()

        html = response.text

        return {
            "success": True,
            "status_code": response.status_code,
            "url": url,
            "html": html,
        }

    except requests.RequestException as error:
        return {
            "success": False,
            "url": url,
            "error": str(error),
        }


def extract_ean(html: str) -> str | None:
    """
    Extract an EAN from the supplier page.
    """

    patterns = [
        r'<div\s+class="barcodetext">\s*(\d{13})\s*</div>',
        r'<div\s+class=["\']barcodetext["\'][^>]*>\s*(\d{13})\s*</div>',
        r'barcodetext[^>]*>\s*(\d{13})\s*<',
    ]

    for pattern in patterns:
        match = re.search(pattern, html, re.IGNORECASE)

        if match:
            return match.group(1)

    return None

def extract_supplier_price(html: str) -> float | None:
    """
    Extract the reduced supplier price from the product page.
    """

    pattern = r'<ins class="blue"><span>Reduced:\s*</span>&pound;([\d.]+)</ins>'

    match = re.search(pattern, html, re.IGNORECASE)

    if match:
        return float(match.group(1))

    return None

    for pattern in patterns:
        match = re.search(pattern, html, re.IGNORECASE)

        if match:
            return match.group(1)

    return None

def extract_pack_size(html: str) -> int | None:
    """
    Extract the pack size from the supplier product page.
    """

    pattern = r'(\d+)\s*x\s+Bourjois'

    match = re.search(pattern, html, re.IGNORECASE)

    if match:
        return int(match.group(1))

    return None

def extract_product_name(html: str) -> str | None:
    """
    Extract the product name from the supplier page.
    """

    pattern = r'<h1[^>]*>(.*?)</h1>'

    match = re.search(pattern, html, re.IGNORECASE | re.DOTALL)

    if match:
        name = re.sub(r'<[^>]+>', '', match.group(1))
        name = " ".join(name.split())
        return name.strip()

    return None

def extract_stock(html: str) -> int | None:
    """
    Extract the available stock quantity from the supplier page.
    """

    patterns = [
        r'var\s+stock\s*=\s*(\d+)',
        r'(\d+)\s+in stock',
        r'(\d+)\s+available',
        r'Stock:\s*(\d+)',
    ]

    for pattern in patterns:
        match = re.search(pattern, html, re.IGNORECASE)

        if match:
            return int(match.group(1))

    return None

def get_product_data(url: str) -> dict:
    """
    Retrieve and extract all available supplier product data.
    """

    result = get_supplier_product(url)

    if not result["success"]:
        return result

    html = result["html"]

    return {
        "success": True,
        "url": url,
        "product_name": extract_product_name(html),
        "ean": extract_ean(html),
        "price": extract_supplier_price(html),
        "pack_size": extract_pack_size(html),
        "stock": extract_stock(html),
    }