import pytest

from src.pages.login.loginpage import LoginPage
from src.navigation import Navigation

# from src import shapes

# @pytest.fixture
# def my_rectangle():
#     return shapes.Rectangle(10, 5)

# @pytest.fixture
# def other_rectangle():
#     return shapes.Rectangle(20, 2)

@pytest.fixture(scope="class")
def navigation():
    return Navigation()

@pytest.fixture(scope="class")
def login_page():
    return LoginPage()
