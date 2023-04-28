from sqlalchemy.orm import Session
from sqlalchemy import select, delete

from src.db import get_db
from src.models.products import DAOProducts, ProductsModel


class Products:
    prod: ProductsModel

    def __init__(self, data: ProductsModel):
        self.prod = data

    def create_product(self, user_id: int = 3):
        sess: Session = next(get_db())

        # MySQL 한글 처리 필요
        product = DAOProducts(category=self.prod.category,
                              price=self.prod.price,
                              cost=self.prod.cost,
                              name=self.prod.name,
                              description=self.prod.description,
                              barcode=self.prod.barcode,
                              expiration_data=self.prod.expiration_data,
                              size=self.prod.size,
                              user_id=user_id)
        print(product.__repr__())
        sess.add(product)
        sess.commit()

        # 성공 여부를 확인하는 부분이 필요함.
        return "OK"
