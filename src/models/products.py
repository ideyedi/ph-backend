from typing import Optional
from pydantic import BaseModel
from src.config import product_sizes
from datetime import date


class ProductModel(BaseModel):
    category: str
    price: int
    cost: int
    name: str
    description: Optional[str]
    barcode: str
    expiration_data: date
    size: product_sizes
