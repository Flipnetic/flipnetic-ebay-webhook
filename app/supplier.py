from dataclasses import dataclass

from app.supplier_settings import SupplierSettings


@dataclass
class SupplierProduct:
    supplier: str
    ean: str
    product_name: str
    pack_size: int
    price: float
    settings: SupplierSettings
    stock: int = 0
    product_url: str = ""

    @property
    def price_excluding_vat(self) -> float:
        if self.settings.prices_include_vat:
            return round(
                self.price / (1 + self.settings.vat_rate / 100),
                2,
            )

        return round(self.price, 2)

    @property
    def vat_amount(self) -> float:
        return round(
            self.price_excluding_vat
            * (self.settings.vat_rate / 100),
            2,
        )

    @property
    def price_including_vat(self) -> float:
        return round(
            self.price_excluding_vat + self.vat_amount,
            2,
        )

    @property
    def unit_cost_including_vat(self) -> float:
        if self.pack_size <= 0:
            return 0.0

        return round(
            self.price_including_vat / self.pack_size,
            2,
        )