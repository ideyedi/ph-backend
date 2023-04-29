from typing import Optional

from fastapi import (APIRouter,
                     status,
                     HTTPException,
                     Depends
                     )
from fastapi.security import OAuth2PasswordRequestForm

from src.models.users import UsersModel
from src.utils import (get_hashed_pw,
                       decode_hashed_pw,
                       create_access_token,
                       create_refresh_token,
                       )

from src.services.users import Users as UserService
from src.dependency import authentic_user


router = APIRouter(prefix="/users", tags=["users"])


@router.post("")
async def signup_user(id: int, pw: str, des: Optional[str] = None):
    """
    회원 가입
    :param data:
    :return:
    """
    s = UserService(user_id=id, user_pw=pw, description=des)
    ret: UsersModel = s.create()

    return ret


@router.post("/session", summary="login user")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Login
    :param form_data:
    :param user_id:
    :param user_pw:
    :return:
    """
    s = UserService(user_id=form_data.username, user_pw=form_data.password)
    user = s.select()

    print(decode_hashed_pw(form_data.password, user.user_pw))

    if decode_hashed_pw(form_data.password, user.user_pw):
        tokens = {
            "access_token": create_access_token(user.user_id),
            "refresh_token": create_refresh_token(user.user_id),
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        )

    return tokens


@router.get("/me", response_model=UsersModel)
async def get_my_info(user: UsersModel = Depends(authentic_user)):
    return user
