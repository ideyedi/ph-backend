from fastapi import (APIRouter,
                     Depends,
                     HTTPException,
                     )
from fastapi.responses import PlainTextResponse
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, select, delete, insert

from src.db import get_db
from src.models.users import UserModel
from src.utils import (get_hashed_pw,
                       decode_hashed_pw,
                       create_access_token,
                       create_refresh_token,
                       )

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
async def signup_user(data: UserModel):
    """
    회원 가입
    :param data:
    :return:
    """
    sess: Session = next(get_db())

    ret = select(TblUser).filter(TblUser.user_id == f"{data.identify}")
    # 데이터가 있으면 회원가입 불가 처리
    for item in sess.scalars(ret):
        print(item)

    #ret = insert(TblUser).values(user_id=data.identify, user_pw=get_hashed_pw(data.password), description=data.description)
    #print(ret)
    user = TblUser(user_id=data.identify, user_pw=get_hashed_pw(data.password), description=data.description)
    sess.add(user)
    sess.commit()
    
    return "OK"


@router.get("")
async def get_user_info(data: UserModel):
    """
    탈퇴
    :return:
    """
    sess: Session = next(get_db())
    # 아이디 패스워드가 맞는지 확인 후 삭제하는 로직 추가 필요
    ret = delete(TblUser).filter(TblUser.user_id == f"{data.identify}")

    for item in sess.scalars(ret):
        print(item)

    pass


@router.post("/session", response_class=PlainTextResponse, summary="login user")
async def login_user(user_id: int, user_pw: str):
    """
    Login
    :param user_id:
    :param user_pw:
    :return:
    """
    sess: Session = next(get_db())

    ret = select(TblUser).filter(TblUser.user_id == f"{user_id}")

    # 아이디가 없으면 로그인 불가 처리
    for item in sess.scalars(ret):
        print(item)

    pass


@router.delete("/session", response_class=PlainTextResponse, summary="logout user")
async def logout_user():
    """
    Logout
    :return:
    """
    pass
