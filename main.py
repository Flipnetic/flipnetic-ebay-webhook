from app.profit import calculate_profit
from app.score import calculate_score
from app.decision import get_decision
from app.ean_lookup import lookup_ean
from app.supplier import SupplierProduct
from app.supplier_settings import SupplierSettings
from app.supplier_connector import get_product_data


SUPPLIER_URL = "https://www.wholesale-cosmetics.co.uk/product/9-x-bourjois-twist-extreme-fiber-mascara--024-black/8279/"


ean = input("Enter product EAN: ").strip()

lookup = lookup_ean(ean)

print()
print(f"Flipnetic is checking EAN: {ean}")
print()

if not lookup["found"]:
    print(f"EAN lookup: {lookup['error']}")
    raise SystemExit

print(f"Product found: {lookup['name']}")
print(f"Brand: {lookup['brand']}")
print()

supplier_data = get_product_data(SUPPLIER_URL)

if not supplier_data["success"]:
    print("Supplier data could not be retrieved.")
    raise SystemExit

if supplier_data["ean"] != ean:
    print("Supplier EAN does not match the EAN entered.")
    raise SystemExit

supplier_settings = SupplierSettings(
    supplier_name="Wholesale Cosmetics",
    vat_rate=20.0,
    prices_include_vat=False,
)

supplier_product = SupplierProduct(
    supplier="Wholesale Cosmetics",
    ean=supplier_data["ean"],
    product_name=supplier_data["product_name"],
    pack_size=supplier_data["pack_size"],
    price=supplier_data["price"],
    settings=supplier_settings,
    stock=supplier_data["stock"],
    product_url=SUPPLIER_URL,
)


result = calculate_profit(
    buy_price=supplier_product.unit_cost_including_vat,
    sale_price=7.37,
    ebay_fee=1.10,
    postage=1.50,
)


score = calculate_score(
    profit=result["profit"],
    roi=result["roi"],
    sales_count=2,
    competition=7,
)

decision = get_decision(score)


print("================================")
print("       FLIPNETIC PRODUCT CHECK")
print("================================")
print()
print(f"EAN:             {supplier_product.ean}")
print(f"Product:         {supplier_product.product_name}")
print(f"Supplier:        {supplier_product.supplier}")
print()
print(f"Pack size:       {supplier_product.pack_size}")
print(f"Supplier price:  £{supplier_product.price:.2f}")
print(f"VAT:             £{supplier_product.vat_amount:.2f}")
print(f"Unit cost:       £{supplier_product.unit_cost_including_vat:.2f}")
print(f"Stock:           {supplier_product.stock}")
print()
print(f"Net profit:      £{result['profit']:.2f}")
print(f"ROI:             {result['roi']:.2f}%")
print(f"Flipnetic Score: {score}/100")
print(f"Decision:        {decision}")