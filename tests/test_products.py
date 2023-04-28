import pytest


@pytest.fixture
def get_env():
    import os
    return os.environ["PYENV_VERSION"]


def test_python_version():
    from src.version import __py_ver__
    import sys
    assert sys.version_info >= (3, 8)
