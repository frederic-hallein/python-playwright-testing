import pytest
import yaml

from playwright.sync_api import Page

from src.pages.login.loginpage import LoginPage
from src.pages.homepage.homepage import HomePage

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def home_page(page: Page) -> HomePage:
    return HomePage(page)