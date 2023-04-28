from fastapi import (APIRouter,
                     Depends,
                     )
from typing import Optional

from src.models.products import ProductsModel
from src.services.products import Products as ProdService

from src.models.users import UsersModel
from src.dependency import authentic_user

router = APIRouter(prefix="/products", tags=["products"])


@router.post("")
async def create_product(data: ProductsModel, user: UsersModel = Depends(authentic_user)):
    s = ProdService(data)
    ret = s.create()

    return {"products": ret}


@router.get("")
async def get_product(page: Optional[int] = 1, user: UsersModel = Depends(authentic_user)):
    s = ProdService(ProductsModel)
    print(user.id, page)
    ret = s.get_by_userId(user_id=user.id, page=page)
    print(ret)
    return ret


@router.delete("")
async def delete_product(prod_id: int, user: UsersModel = Depends(authentic_user)):
    s = ProdService(ProductsModel)
    ret = s.delete(prod_id)
    print(ret)
    return ret


@router.patch("")
async def update_product(prod_id: int, data: ProductsModel, user: UsersModel = Depends(authentic_user)):
    # JWT에 해당하는 유저에 따라서 값을 조회하도록 구현
    s = ProdService(data)
    ret = s.update(prod_id, data)
    print(ret)

    return ret
