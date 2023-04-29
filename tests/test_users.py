import pytest
import logging

logger = logging.getLogger('test')


@pytest.fixture
def make_model():
    from src.models.users import UsersModel
    return UsersModel(id=0, user_id=int("01012341234"), user_pw="1234", description="TestCode")


def test_insert_user(make_model):
    from src.services.users import Users as UserService
    user = make_model

    s = UserService(user)
    logger.info(f"{s.user_id}, {s.user_pw}, {s.description}")

    ret = s.create()

    assert ret.user_id == make_model.user_id
