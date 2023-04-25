from fastapi import (APIRouter,
                     Depends,
                     HTTPException,
                     )
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

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


@router.post("")
async def signup_user():
    pass


@router.get("")
async def get_user_info():
    ret = 0
    sess: Session = get_db()
    ret = sess.query(TblUser).all()
    print(ret)
    pass


@router.post("/session", response_class=PlainTextResponse, summary="login user")
async def login_user():
    pass


@router.delete("/session", response_class=PlainTextResponse, summary="logout user")
async def logout_user():
    pass
