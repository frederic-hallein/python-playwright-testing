"""
Should contain custom excepts, i.e. excepts that don't use 
the auto-retrying feature from Playwright.
(See https://playwright.dev/python/docs/test-assertions)
"""

def expect_equality(value_1, value_2) -> None:
    if value_1 != value_2:
        raise AssertionError(f"Expected equality, but got the following instead: \nValue 1: {value_1} \nValue 2: {value_2}")