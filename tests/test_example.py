
import time
import pytest
from src import my_functions

import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))

def test_divide():
    x = 1
    y = 5
    actual = my_functions.divide(x, y)
    expected = x / y
    assert actual == expected, f"Expected {expected}, but got {actual} instead"

def test_divide_by_zero():
    x = 5
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(x, 0)

@pytest.mark.skip(reason="takes too long")
def test_very_slow():
    time.sleep(5)
    x = 1
    y = 2
    actual = my_functions.divide(x, y)
    expected = x / y
    assert actual == expected, f"Expected {expected}, but got {actual} instead"