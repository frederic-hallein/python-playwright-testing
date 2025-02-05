import pytest
# from src import shapes
from src.pages.login.loginpage import LoginPage

# @pytest.fixture
# def my_rectangle():
#     return shapes.Rectangle(10, 5)

# @pytest.fixture
# def other_rectangle():
#     return shapes.Rectangle(20, 2)

@pytest.fixture(scope="class")
def login_page():
    return LoginPage()