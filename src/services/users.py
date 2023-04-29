from typing import Optional

from fastapi import (status, HTTPException)

from sqlalchemy.orm import Session
from sqlalchemy import select, delete

from src.db import get_db
from src.models.users import DAOUsers, UsersModel
from src.utils import (get_hashed_pw,
                       decode_hashed_pw,
                       create_access_token,
                       create_refresh_token,
                       )


class Users:
    user_id: int
    user_pw: str
    description: str

    def __init__(self, user_id: str, user_pw: str = None, description: Optional[str] = None):
        self.user_id = user_id
        self.user_pw = user_pw
        self.description = description

    def select(self) -> UsersModel:
        sess: Session = next(get_db())

        ret = sess.scalar(select(DAOUsers).filter(DAOUsers.user_id == f"{self.user_id}"))
        if ret is None:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Founded id")

        print(ret)
        return UsersModel(id=ret.id,
                          user_id=ret.user_id,
                          user_pw=ret.user_pw,
                          description=ret.description)

    def delete(self):
        sess: Session = next(get_db())
        # 아이디 패스워드가 맞는지 확인 후 삭제하는 로직 추가 필요
        ret = delete(DAOUsers).filter(DAOUsers.user_id == f"{self.user_id}")
        print(ret)

        return ret

    def create(self) -> UsersModel:
        sess: Session = next(get_db())

        ret = sess.scalar(select(DAOUsers).filter(DAOUsers.user_id == f"{self.user_id}"))
        if ret is not None:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Already used ID")

        user = DAOUsers(user_id=self.user_id, user_pw=get_hashed_pw(self.user_pw), description=self.description)
        print(user.__repr__())
        sess.add(user)
        sess.commit()

        # Check Create
        ret = select(DAOUsers).filter(DAOUsers.user_id == f"{self.user_id}")
        return UsersModel(id=sess.scalar(ret).id,
                          user_id=sess.scalar(ret).user_id,
                          user_pw=sess.scalar(ret).user_pw,
                          description=sess.scalar(ret).description)

    def update(self):
        pass
