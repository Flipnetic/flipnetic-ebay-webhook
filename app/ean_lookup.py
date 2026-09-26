import os

import requests
from dotenv import load_dotenv


load_dotenv()


def lookup_ean(ean: str) -> dict:
    """
    Look up an EAN on eBay using the Browse API.
    """

    ean = ean.strip()

    if not ean:
        return {
            "found": False,
            "error": "No EAN was entered.",
        }

    token = os.getenv("EBAY_OAUTH_TOKEN")

    if not token:
        return {
            "found": False,
            "error": "eBay OAuth token is missing.",
        }

    url = "https://api.ebay.com/buy/browse/v1/item_summary/search"

    headers = {
        "Authorization": f"Bearer {token}",
        "X-EBAY-C-MARKETPLACE-ID": "EBAY_GB",
        "Accept": "application/json",
    }

    params = {
        "q": "Bourjois Twist Extreme Fiber Mascara 024 Black",
        "limit": 20,
        "filter": "deliveryCountry:GB",
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=20,
        )

        response.raise_for_status()

        data = response.json()

    except requests.RequestException as error:
        return {
            "found": False,
            "ean": ean,
            "error": f"eBay API request failed: {error}",
        }

    except ValueError:
        return {
            "found": False,
            "ean": ean,
            "error": "eBay returned an invalid response.",
        }

    items = data.get("itemSummaries", [])

    if not items:
        return {
            "found": False,
            "ean": ean,
            "error": "No eBay listings were found for this EAN.",
        }

    first_item = items[0]

    return {
        "found": True,
        "ean": ean,
        "name": first_item.get("title", "Unknown product"),
        "brand": first_item.get("brand"),
        "listing_count": len(items),
        "total_results": data.get("total", len(items)),
        "items": items,
    }