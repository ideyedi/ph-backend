from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from sqlalchemy import select, delete, insert, update

from src.config import pagination
from src.db import get_db
from src.models.products import DAOProducts, ProductsModel


class Products:
    prod: ProductsModel
    user_id: int

    def __init__(self, data: ProductsModel):
        self.prod = data

    def create(self):
        sess: Session = next(get_db())

        product = DAOProducts(category=self.prod.category,
                              price=self.prod.price,
                              cost=self.prod.cost,
                              name=self.prod.name,
                              description=self.prod.description,
                              barcode=self.prod.barcode,
                              expiration_date=self.prod.expiration_date,
                              size=self.prod.size,
                              user_id=self.user_id)
        print(product.__repr__())
        sess.add(product)
        sess.commit()

        # Need to success check
        return "OK"

    def get_by_user_id(self, page: int = 1) -> List[ProductsModel]:
        result = []

        sess: Session = next(get_db())
        ret = select(DAOProducts).where(DAOProducts.user_id == f"{self.user_id}")

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
                                  expiration_data=item.expiration_date,
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

    def get_by_prod_name(self):
        searched = []
        sess: Session = next(get_db())
        """
        ret = sess.execute(select(DAOProducts)
                           .where(DAOProducts.user_id == f"{self.user_id}")
                           .where(DAOProducts.name.like(f"%{self.prod.name}%"))
                           .where(DAOProducts.name.rlike(f"^ㄴ") or (DAOProducts.name >= '나' and DAOProducts < '다'))
                           )
        """
        r_sql = text(f"""
        """)

        print(__name__, self.prod.name)
        print(__name__, r_sql)

        ret = sess.execute(r_sql)
        for item in ret:
            print(item)
            searched.append((item))

        return searched

    def get_by_cho(self):
        pass

    def update(self, prod_id: int, data: ProductsModel):
        sess: Session = next(get_db())
        ret = sess.execute(update(DAOProducts)
                           .where(DAOProducts.id == f"{prod_id}")
                           .where(DAOProducts.user_id == f"{self.user_id}")
                           .values(category=f"{data.category}",
                                   name=f"{data.name}",
                                   price=f"{data.price}",
                                   cost=f"{data.cost}",
                                   description=f"{data.description}",
                                   barcode=f"{data.barcode}",
                                   expiration_date=f"{data.expiration_date}"))

        # user의 product 아닐때 raise error 처리해주면 더 좋을 듯
        sess.commit()
        return ret

    def delete(self, prod_id: int):
        sess: Session = next(get_db())
        ret = sess.execute(delete(DAOProducts)
                           .where(DAOProducts.id == f"{prod_id}")
                           .where(DAOProducts.user_id == f"{self.user_id}"))
        # user의 product 아닐때 raise error 처리해주면 더 좋을 듯
        sess.commit()
        return ret
