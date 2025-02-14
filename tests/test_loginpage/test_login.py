import pytest

from utils.helper import yaml_loader
from utils.helper import generate_random_string

users = yaml_loader("res/users.yaml").values()
page_section = ["inventory", "cart", "checkout-step-one", "checkout-step-two", "checkout-complete"]

class TestLogin:
    @pytest.mark.url
    def test_correct_url(self, login_page) -> None:
        # ACTIONS ------------------------------------

        # ASSERTIONS ------------------------------------
        login_page.expect_title_to_have_text("Swag Labs")
        login_page.expect_login_page_to_be_visible()

    @pytest.mark.login
    @pytest.mark.parametrize(("username", "password"), users)
    def test_log_in(self, login_page, inventory_page, username, password) -> None:
        # ACTIONS ------------------------------------
        login_page.log_in(username, password)

        # ASSERTIONS ------------------------------------
        if username == "locked_out_user":
            login_page.expect_error_message("Epic sadface: Sorry, this user has been locked out.")
        else:
            inventory_page.expect_inventory_page_to_be_visible()

    @pytest.mark.invalid_login
    def test_invalid_log_in(self, login_page) -> None:
        # ACTIONS ------------------------------------
        random_username = generate_random_string()
        random_password = generate_random_string()
        login_page.log_in(random_username, random_password)

        # ASSERTIONS ------------------------------------
        login_page.expect_error_message("Epic sadface: Username and password do not match any user in this service")

    @pytest.mark.cannot_access_without_login
    @pytest.mark.parametrize("page_section", page_section)
    def test_cannot_access_site_without_logging_in(self, login_page, page_section) -> None:
        # ACTIONS ------------------------------------
        login_page.navigate_to(page_section)

        # ASSERTIONS ------------------------------------
        login_page.expect_error_message(f"Epic sadface: You can only access '/{page_section}.html' when you are logged in.")