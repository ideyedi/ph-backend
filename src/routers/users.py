from fastapi import (APIRouter,
                     Depends,
                     HTTPException,
                     )
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, select

from src.db import get_db
from src.models.users import UserModel

import requests

router = APIRouter(prefix="/users", tags=["users"])

Base = declarative_base()


class TblUser(Base):
    __tablename__ = "tbl_user"

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    user_pw = Column(String)
    description = Column(String)

    def __repr__(self) -> str:
        return f"User(id={self.id}, user_id={self.user_id}, user_pw={self.user_pw}, description={self.description})"


@router.post("")
async def signup_user():
    pass


@router.get("")
async def get_user_info():
    ret = 0
    print('1')
    sess: Session = next(get_db())
    print('2')
    ret = select(TblUser)
    print('3')

    print(ret)
    for item in sess.scalars(ret):
        print(item)

    pass


@router.post("/session", response_class=PlainTextResponse, summary="login user")
async def login_user():
    pass


@router.delete("/session", response_class=PlainTextResponse, summary="logout user")
async def logout_user():
    pass
