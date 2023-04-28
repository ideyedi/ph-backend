from typing import Optional, Literal
from pydantic import BaseModel
from datetime import date

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

from src.config import product_sizes


Base = declarative_base()


class DAOProducts(Base):
    __tablename__ = "tbl_products"

    id = Column(Integer, primary_key=True)
    category = Column(String)
    price = Column(Integer)
    cost = Column(Integer)
    name = Column(String)
    description = Column(String)
    barcode = Column(String)
    expiration_data = Column(DateTime)
    size = Column(String)
    user_id = Column(Integer)

    def __repr__(self) -> str:
        return f"Products(id={self.id}, name={self.name}, user={self.user_id})"


class ProductsModel(BaseModel):
    category: str
    price: int
    cost: int
    name: str
    description: Optional[str]
    barcode: str
    expiration_data: date
    size: Literal["small", "large"] = "small"
