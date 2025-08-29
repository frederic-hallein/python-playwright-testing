"""
Tests for the login page functionality.
"""

import random
import pytest

from utils.helper import generate_random_string

class TestLoginPage:
    """
    Test suite for login page scenarios.
    """
    @pytest.mark.url
    def test_correct_url(self, login_page) -> None:
        """Test that the login page loads with the correct URL and elements."""
        # ARRANGE ------------------------------------

        # ACT ------------------------------------
        login_page.navigate_to()

        # ASSERT ------------------------------------
        login_page.expect_title_to_have_text("Swag Labs")
        login_page.expect_login_page_to_be_visible()

    @pytest.mark.locked_out_user_login
    def test_locked_out_user_login(self, login_page) -> None:
        """Test login with a locked out user and verify error message."""
        # ARRANGE ------------------------------------
        username = "locked_out_user"
        password = "secret_sauce"

        # ACT ------------------------------------
        login_page.log_in(username, password)

        # ASSERT ------------------------------------
        login_page.expect_error_message("Epic sadface: Sorry, this user has been locked out.")

    @pytest.mark.valid_user_login
    def test_user_login(self, login_page, users, inventory_page) -> None:
        """Test login with a valid user and verify inventory page is visible."""
        # ARRANGE ------------------------------------
        usernames = users["userName"]
        username = random.choice(usernames)
        password = users["password"]

        # ACT ------------------------------------
        login_page.log_in(username, password)

        # ASSERT ------------------------------------
        inventory_page.expect_inventory_page_to_be_visible()

    @pytest.mark.invalid_user_login
    def test_invalid_user_login(self, login_page) -> None:
        """Test login with invalid credentials and verify error message."""
        # ARRANGE ------------------------------------
        random_username = generate_random_string()
        random_password = generate_random_string()

        # ACT ------------------------------------
        login_page.log_in(random_username, random_password)

        # ASSERT ------------------------------------
        login_page.expect_error_message(
            "Epic sadface: Username and password do not match any user in this service")
