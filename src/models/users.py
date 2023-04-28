from typing import Optional
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, select, delete


Base = declarative_base()


class DAOUsers(Base):
    __tablename__ = "tbl_user"

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    user_pw = Column(String)
    description = Column(String)

    def __repr__(self) -> str:
        return f"User(id={self.id}, user_id={self.user_id}, user_pw={self.user_pw}, description={self.description})"


class ModelUsers(BaseModel):
    user_id: int
    user_pw: str
    description: Optional[str]
