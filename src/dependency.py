from typing import Union, Any, Optional
from datetime import datetime

from fastapi import (status, HTTPException, Depends,)
from fastapi.security import OAuth2PasswordBearer

from jose import jwt
from pydantic import ValidationError

from src.models.tokens import TokenSchema, TokenPayload
from src.models.users import UsersModel

from src.utils import (ALGORITHM, JWT_SECRET_KEY,)
from src.services.users import Users as UserService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/session")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)
        print(token_data.sub)

        # Token time check
        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="",
            headers="",
        )

    s = UserService(UsersModel)
    s.user_id = token_data.sub
    user: UsersModel = s.select_user()
    print(user.user_id, user.description)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )

    return UsersModel(**user)
