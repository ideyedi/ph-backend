import pytest
import logging

logger = logging.getLogger('test')


@pytest.fixture
def get_env():
    import os
    return os.environ["PYENV_VERSION"]


def test_python_version():
    from src.version import __py_ver__
    import sys
    logger.info(sys.version_info)
    assert sys.version_info >= __py_ver__
