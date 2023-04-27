from passlib.context import CryptContext
from jose import jwt
from typing import Union, Any
from datetime import datetime, timedelta

pw_context = CryptContext(schemes=["bcrypt"])
ACCESS_TOKEN_EXPIRE_M = 30
REFRESH_TOKEN_EXPIRE_M = 60 * 24
ALGORITHM = "HS256"
JWT_SECRET_KEY = "access_secret"
JWT_REFRESH_SECRET_KEY = "refresh_secret"


def get_hashed_pw(user_pw: str) -> str:
    ret = pw_context.hash(user_pw)
    print(ret)
    return ret


def decode_hashed_pw(input_pw: str, hashed_pw: str) -> bool:
    return pw_context.verify(input_pw, hashed_pw)


def create_access_token(subject: Union[str, Any], expire_delta: int = None) -> str:

    if expire_delta is not None:
        expire_delta = datetime.utcnow() + expire_delta
    else:
        expire_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_M)

    to_encode = {"exp": expire_delta, "sub": str(subject)}
    jwt_encode = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    print(jwt_encode)

    return jwt_encode


def create_refresh_token(subject: Union[str, Any], expire_delta: int = None) -> str:

    if expire_delta is not None:
        expire_delta = datetime.utcnow() + expire_delta
    else:
        expire_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_M)

    to_encode = {"exp": expire_delta, "sub": str(subject)}
    jwt_encode = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    print(jwt_encode)

    return jwt_encode
