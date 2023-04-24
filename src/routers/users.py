from fastapi import (APIRouter,
                     HTTPException,
                     )
from fastapi.responses import PlainTextResponse
from src.models.users import UserModel

import requests
