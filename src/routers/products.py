from fastapi import (APIRouter,
                     Depends,
                     HTTPException,
                     status
                     )
from fastapi.security import OAuth2PasswordBearer
from typing import Optional

from src.models.products import ProductsModel
from src.services.products import Products as ProdService

router = APIRouter(prefix="/products", tags=["products"])


@router.post("")
async def create_product(data: ProductsModel):
    s = ProdService(data)
    ret = s.create()

    return {"products": ret}


@router.get("")
async def get_product(user_id: Optional[int] = 3, page: Optional[int] = 1):
    s = ProdService(ProductsModel)
    print(user_id, page)
    ret = s.get_by_userId(user_id=user_id, page=page)
    print(ret)
    return ret


@router.delete("")
async def delete_product(prod_id: int):
    s = ProdService(ProductsModel)
    ret = s.delete(prod_id)
    print(ret)
    return ret


@router.patch("")
async def update_product(prod_id: int, data: ProductsModel):
    # JWT에 해당하는 유저에 따라서 값을 조회하도록 구현
    s = ProdService(data)
    ret = s.update(prod_id, data)
    print(ret)

    return ret
