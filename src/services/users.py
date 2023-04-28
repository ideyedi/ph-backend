from sqlalchemy.orm import Session
from sqlalchemy import select, delete

from src.db import get_db
from src.models.users import DAOUsers, UsersModel


class Users:

    def __init__(self, user_id: str, user_pw: str = None):
        self.user_id = user_id
        self.user_pw = user_pw

    def _check_user_info(self):
        """
        User id, pw 일치 확인 용 Validate function
        :return: Boolean
        """
        pass

    def select_user(self) -> UsersModel:
        sess: Session = next(get_db())

        # 아이디가 없으면 로그인 불가 처리, 데이터가 없을 경우 예외 처리도 필요
        ret = select(DAOUsers).filter(DAOUsers.user_id == f"{self.user_id}")

        return UsersModel(id=sess.scalar(ret).id,
                          user_id=sess.scalar(ret).user_id,
                          user_pw=sess.scalar(ret).user_pw,
                          description=sess.scalar(ret).description)

    def delete_user(self):
        sess: Session = next(get_db())
        # 아이디 패스워드가 맞는지 확인 후 삭제하는 로직 추가 필요
        ret = delete(DAOUsers).filter(DAOUsers.user_id == f"{self.user_id}")
        print(ret)

        return ret

    def create_user(self):
        pass

    def update_user(self):
        pass
