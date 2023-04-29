from fastapi import (APIRouter,
                     Depends,
                     )
from typing import Optional

from src.models.products import ProductsModel
from src.services.products import Products as ProdService

from src.models.users import UsersModel
from src.dependency import authentic_user
from src.config import COMPATIBILITY_CHOSUNG

router = APIRouter(prefix="/products", tags=["products"])


@router.post("")
async def create_product(data: ProductsModel, user: UsersModel = Depends(authentic_user)):
    print(__name__)
    s = ProdService(data)
    s.user_id = user.id
    ret = s.create()

    return {"products": ret}


@router.get("")
async def get_product(page: Optional[int] = 1, user: UsersModel = Depends(authentic_user)):
    s = ProdService(ProductsModel)
    s.user_id = user.id

    print(user.id, page)
    ret = s.get_by_user_id(page=page)
    print(ret)
    return ret


@router.delete("")
async def delete_product(prod_id: int, user: UsersModel = Depends(authentic_user)):
    s = ProdService(ProductsModel)
    s.user_id = user.id

    ret = s.delete(prod_id)
    print(__name__, ret)
    return ret


@router.patch("")
async def update_product(prod_id: int, data: ProductsModel, user: UsersModel = Depends(authentic_user)):
    # JWT에 해당하는 유저에 따라서 값을 조회하도록 구현
    s = ProdService(data)
    s.user_id = user.id

    print(__name__, s.user_id)
    ret = s.update(prod_id, data)
    print(ret)

    return ret


@router.get("/search")
async def search_by_name(prod_name: str, user: UsersModel = Depends(authentic_user)):
    """
    'prod_name' 값에 따라 초성 검색 여부를 구분
    :param prod_name:
    :param user:
    :return:
    """
    s = ProdService(ProductsModel)
    s.prod.name = prod_name
    s.user_id = user.id

    if prod_name[0] in COMPATIBILITY_CHOSUNG:
        print('cho')
        ret = s.get_by_cho()
    else:
        print('normal')
        ret = s.get_by_prod_name()

    return "OK"
