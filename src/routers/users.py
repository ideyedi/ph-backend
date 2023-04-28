from fastapi import (APIRouter,
                     Depends,
                     HTTPException,
                     )
from fastapi.responses import PlainTextResponse
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from sqlalchemy import select, delete

from src.db import get_db
from src.models.users import UserModel, TblUser
from src.utils import (get_hashed_pw,
                       decode_hashed_pw,
                       create_access_token,
                       create_refresh_token,
                       )

router = APIRouter(prefix="/users", tags=["users"])


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

    user = TblUser(user_id=data.identify, user_pw=get_hashed_pw(data.password), description=data.description)
    # Commit & Save
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
        print(int(item.user_id), str(item.user_pw), item.description)
        user = UserModel(identify=int(item.user_id), password=str(item.user_pw), decription=str(item.description))

    print(user)
    print(user.identify, user.password, user.description)
    print(decode_hashed_pw(user_pw, user.password))
    if decode_hashed_pw(user_pw, user.password):
        tokens = {
            "access_token": create_access_token(user.identify),
            "refresh_token": create_refresh_token(user.identify),
        }

    return "OK"


@router.delete("/session", response_class=PlainTextResponse, summary="logout user")
async def logout_user():
    """
    Logout
    :return:
    """
    pass
