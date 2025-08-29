import pytest
import yaml
import os.path
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from collections.abc import Generator

from playwright.sync_api import Browser, Page

from utils.helper import yaml_loader

from src.pages.loginpage.loginpage import LoginPage
from src.pages.inventorypage.inventorypage import InventoryPage

def pytest_collection_modifyitems(items):
    """ Modifies test items in place to ensure test classes run in a given order. """
    CLASS_ORDER = [
        "TestLoginPage",
        "TestInventoryPage"
    ]
    sorted_items = items.copy()
      # read the class names from default items
    class_mapping = {item: item.cls.__name__ for item in items}

    # Iteratively move tests of each class to the end of the test queue
    for class_ in CLASS_ORDER:
        sorted_items = [it for it in sorted_items if class_mapping[it] != class_] + [
            it for it in sorted_items if class_mapping[it] == class_
        ]
    items[:] = sorted_items

@pytest.fixture(scope="session")
def base() -> str:
    return yaml.load(open("res/urls.yaml"), Loader=yaml.FullLoader).get("base")

@pytest.fixture
def users() -> list[str]:
    return yaml_loader("res/users.yaml")

@pytest.fixture(scope="session")
def page(browser: Browser, base) -> Generator[Page, None, None]:
    path = "playwright/.auth/storage_state.json"
    if os.path.exists(path):
        context = browser.new_context(storage_state=path)
    else:
        context = browser.new_context()
    page = context.new_page()
    page.goto(base)
    yield page
    context.storage_state(path=path)
    page.close()
    context.close()

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    return InventoryPage(page)
