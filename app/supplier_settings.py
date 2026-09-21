from dataclasses import dataclass


@dataclass
class SupplierSettings:
    supplier_name: str
    vat_rate: float = 20.0
    prices_include_vat: bool = False