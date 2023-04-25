from typing import Optional
from pydantic import BaseModel


class UserModel(BaseModel):
    id: int
    identify: int
    password: str
    description: Optional[str]
