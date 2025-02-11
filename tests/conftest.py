import pytest
import yaml
import json
from collections.abc import Generator

from playwright.sync_api import sync_playwright, Page

from src.pages.loginpage.loginpage import LoginPage
from src.pages.homepage.homepage import HomePage

base = yaml.load(open("res/urls.yaml"), Loader=yaml.FullLoader)["urls"]["base"]
# storages = []

# TODO : 
# (1) check if storage state file empty. If empty, save storage state, else make new context using storage state of specific user
# (2) yield this page
@pytest.fixture
def page() -> Generator[Page, None, None]:
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(base)
    yield page
    # storage = context.storage_state() #path="playwright/.auth/state.json"
    # storages.append(storage)
    # if len(storages) == 6:
    #     with open('playwright/.auth/state.json', 'w') as outfile:
    #         json.dump(storages, outfile)

    # context = browser.new_context(storage_state=storage)

    page.close()
    context.close()
    browser.close()
    p.stop()

@pytest.fixture
def login_page(page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def home_page(page) -> HomePage:
    return HomePage(page)