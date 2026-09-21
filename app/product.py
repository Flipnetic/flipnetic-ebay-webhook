from dataclasses import dataclass


@dataclass
class Product:
    ean: str
    name: str
    buy_price: float
    average_sold_price: float
    sales_count: int
    competition: int
    profit: float = 0.0
    roi: float = 0.0
    score: int = 0
    decision: str = "PASS"