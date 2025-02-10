import pytest

from src.common import generate_random_string

@pytest.mark.login
@pytest.mark.parametrize("username", ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user", "error_user", "visual_user"])
def test_log_in(login_page, home_page, username) -> None:
    login_page.navigate_to()
    login_page.expect_correct_title("Swag Labs")
    login_page.expect_login_page_to_be_visible()

    login_page.log_in(username, "secret_sauce")
    if username == "locked_out_user":
        login_page.expect_error_message("Epic sadface: Sorry, this user has been locked out.")
    else:
        home_page.expect_home_page_to_be_visible()

@pytest.mark.invalid_login
def test_invalid_log_in(login_page) -> None:
    login_page.navigate_to()
    random_username = generate_random_string()
    random_password = generate_random_string()
    login_page.log_in(random_username, random_password)
    login_page.expect_error_message("Epic sadface: Username and password do not match any user in this service")

@pytest.mark.cannot_acces_without_login
@pytest.mark.parametrize("page_section", ["inventory", "cart", "checkout-step-one", "checkout-step-two", "checkout-complete"])
def test_cannot_access_site_without_logging_in(login_page, page_section) -> None:
    login_page.navigate_to(page_section)
    login_page.expect_error_message(f"Epic sadface: You can only access '/{page_section}.html' when you are logged in.")

@pytest.mark.logout
def test_log_out(login_page, home_page) -> None:
    login_page.navigate_to()
    login_page.log_in("standard_user", "secret_sauce")
    home_page.log_out()
    login_page.expect_login_page_to_be_visible()

    
