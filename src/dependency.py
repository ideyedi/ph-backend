from typing import Union, Any, Optional
from datetime import datetime

from fastapi import (status, HTTPException, Depends,)
from fastapi.security import OAuth2PasswordBearer

from jose import jwt
from pydantic import ValidationError

from src.models.tokens import TokenPayload
from src.models.users import UsersModel

from src.utils import (ALGORITHM, JWT_SECRET_KEY,)
from src.services.users import Users as UserService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/session")


async def authentic_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            # Expired Token Error handled
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    except(jwt.JWTError, ValidationError):
        # Info Validated Error
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

    s = UserService(user_id=token_data.sub, user_pw=None)
    user: UsersModel = s.select()
    print(user)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return user
