from fastapi import (APIRouter,
                     status,
                     HTTPException,
                     )
from fastapi.responses import (PlainTextResponse,
                               JSONResponse,
                               )
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from sqlalchemy import select, delete

from src.db import get_db
from src.models.users import DAOUsers, ModelUsers
from src.utils import (get_hashed_pw,
                       decode_hashed_pw,
                       create_access_token,
                       create_refresh_token,
                       )

from src.services.users import Users as UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.post("")
async def signup_user(data: ModelUsers):
    """
    회원 가입
    :param data:
    :return:
    """
    sess: Session = next(get_db())

    ret = select(DAOUsers).filter(DAOUsers.user_id == f"{data.user_id}")
    # 데이터가 있으면 회원가입 불가 처리
    for item in sess.scalars(ret):
        print(item)

    user = DAOUsers(user_id=data.user_id, user_pw=get_hashed_pw(data.user_pw), description=data.description)
    # Commit & Save
    sess.add(user)
    sess.commit()

    return "OK"


@router.get("")
async def get_user_info(data: ModelUsers):
    """
    탈퇴
    :return:
    """
    o = UserService(user_id=data.user_id)


@router.post("/session", response_class=JSONResponse, summary="login user")
async def login_user(user_id: int, user_pw: str):
    """
    Login
    :param user_id:
    :param user_pw:
    :return:
    """
    o = UserService(user_id=user_id)
    user = o.select_user()
    print(user)
    print(user.user_id, user.user_pw, user.description)
    print(decode_hashed_pw(user_pw, user.user_pw))

    if decode_hashed_pw(user_pw, user.user_pw):
        tokens = {
            "access_token": create_access_token(user.user_id),
            "refresh_token": create_refresh_token(user.user_id),
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        )

    return tokens


@router.delete("/session", response_class=PlainTextResponse, summary="logout user")
async def logout_user():
    """
    Logout
    :return:
    """
    pass
