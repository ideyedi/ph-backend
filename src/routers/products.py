from fastapi import (APIRouter,
                     Depends,
                     HTTPException,
                     status
                     )
from fastapi.responses import PlainTextResponse
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from pydantic import ValidationError
from jose import jwt
from typing import Union, Any, Optional

from src.utils import (ALGORITHM, JWT_SECRET_KEY, JWT_REFRESH_SECRET_KEY)
from src.db import get_db
from src.models.products import DAOProducts, ProductsModel
from src.services.products import Products as ProdService

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/users",
    scheme_name="JWT"
)

router = APIRouter(prefix="/products", tags=["products"])


async def get_current_user(token: str = Depends(reuseable_oauth)):
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )
        #token_data = Token
    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="",
            headers="",
        )
    sess: Session = next(get_db())

    user: Union[dict[str, Any], None]
# ---- JWT Baerer 추가 작업 필요, 일단 기능 구현부터


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
