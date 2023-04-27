from fastapi import (APIRouter,
                     Depends,
                     HTTPException,
                     status
                     )
from fastapi.responses import PlainTextResponse
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, select, delete

from pydantic import ValidationError
from jose import jwt
from typing import Union, Any

from src.utils import (ALGORITHM, JWT_SECRET_KEY, JWT_REFRESH_SECRET_KEY)
from src.db import get_db


reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/users",
    scheme_name="JWT"
)


router = APIRouter(prefix="/products", tags=["products"])

Base = declarative_base()


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



@router.get("", response_class=PlainTextResponse)
async def get_product(prod_name: str):

    return "OK"
