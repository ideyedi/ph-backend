from typing import List

from sqlalchemy.orm import Session
from sqlalchemy import select, delete, insert, update

from src.config import pagination
from src.db import get_db
from src.models.products import DAOProducts, ProductsModel


class Products:
    prod: ProductsModel

    def __init__(self, data: ProductsModel):
        self.prod = data

    def create(self, user_id: int = 3):
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

        # Need to success check
        return "OK"

    def get_by_userId(self, user_id: int, page: int = 1) -> List[ProductsModel]:
        result = []

        sess: Session = next(get_db())
        ret = select(DAOProducts).filter(DAOProducts.user_id == f"{user_id}")

        # Make List & Pagination
        # 쿼리에서 한번에 처리할 수 있으면 더 좋을 거 같은데.
        for item in sess.scalars(ret):
            print(item.__repr__())
            model = ProductsModel(category=item.category,
                                  price=item.price,
                                  cost=item.cost,
                                  name=item.name,
                                  description=item.description,
                                  barcode=item.barcode,
                                  expiration_data=item.expiration_data,
                                  size=item.size)
            result.append(model)

        total = len(result)
        p = total // pagination

        # 구현 후 데이터 넣고 테스트 해보자
        if p == page:
            result = result[page * pagination:]
        elif p == 0:
            result = result[:pagination]
        elif p > page:
            result = result[page * pagination:(page + 1) * pagination]
        else:
            result = []

        return result

    def get_by_prodId(self, prod_id: int) -> ProductsModel:
        sess: Session = next(get_db())
        ret: ProductsModel = sess.scalar(select(DAOProducts).filter(DAOProducts.id == f"{prod_id}"))
        return ret

    def update(self, prod_id: int, data: ProductsModel):
        sess: Session = next(get_db())
        ret = sess.execute(update(DAOProducts)
                           .where(DAOProducts.id == f"{prod_id}")
                           .values(name=f"{data.name}"))

        sess.commit()

        return ret

    def delete(self, prod_id: int):
        sess: Session = next(get_db())
        ret = sess.execute(delete(DAOProducts)
                           .where(DAOProducts.id == f"{prod_id}"))
        sess.commit()
        return ret
