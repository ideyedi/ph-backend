from typing import Optional
from pydantic import BaseModel


class UserModel(BaseModel):
    identify: int
    password: str
    description: Optional[str]
