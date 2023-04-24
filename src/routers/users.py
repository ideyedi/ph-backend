from fastapi import (APIRouter,
                     HTTPException,
                     )
from fastapi.responses import PlainTextResponse
from src.models.users import UserModel

import requests

router = APIRouter(prefix="/users", tags=["users"])


@router.post("")
async def signup_user():
    pass


@router.get("")
async def get_user_info():
    pass


@router.post("/session", response_class=PlainTextResponse, summary="login user")
async def login_user():
    pass


@router.delete("/session", response_class=PlainTextResponse, summary="logout user")
async def logout_user():
    pass
