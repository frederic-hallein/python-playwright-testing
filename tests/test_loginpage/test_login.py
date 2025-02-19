import pytest
import random

from utils.helper import generate_random_string

class TestLoginPage:
    @pytest.mark.url
    def test_correct_url(self, login_page) -> None:
        # ACTIONS ------------------------------------
        login_page.navigate_to()

        # ASSERTIONS ------------------------------------
        login_page.expect_title_to_have_text("Swag Labs")
        login_page.expect_login_page_to_be_visible()

    @pytest.mark.valid_user_login
    def test_user_login(self, login_page, users, inventory_page) -> None:
        usernames = users["userName"]
        usernames.remove("locked_out_user")
        username = random.choice(usernames)
        password = users["password"]

        # ACTIONS ------------------------------------
        login_page.log_in(username, password)

        # ASSERTIONS ------------------------------------
        inventory_page.expect_inventory_page_to_be_visible()

    @pytest.mark.locked_out_user_login
    def test_locked_out_user_login(self, login_page) -> None:
        username = "locked_out_user"
        password = "secret_sauce"

        # ACTIONS ------------------------------------
        login_page.log_in(username, password)

        # ASSERTIONS ------------------------------------
        login_page.expect_error_message("Epic sadface: Sorry, this user has been locked out.")

    @pytest.mark.invalid_user_login
    def test_invalid_user_login(self, login_page) -> None:
        random_username = generate_random_string()
        random_password = generate_random_string()

        # ACTIONS ------------------------------------
        login_page.log_in(random_username, random_password)

        # ASSERTIONS ------------------------------------
        login_page.expect_error_message("Epic sadface: Username and password do not match any user in this service")

