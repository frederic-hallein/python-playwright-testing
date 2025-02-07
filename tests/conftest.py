import pytest
import yaml

from playwright.sync_api import Page

from src.pages.login.loginpage import LoginPage
from src.navigation import Navigation

@pytest.fixture(scope="function")
def user():
    return yaml.load(open("res/user.yaml"), Loader=yaml.FullLoader)["user"]

@pytest.fixture(scope="function")
def navigation(page: Page):
    return Navigation(page)

@pytest.fixture(scope="function")
def login_page(page: Page):
    return LoginPage(page)
