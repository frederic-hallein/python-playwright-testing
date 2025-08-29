"""
Module for the LoginPage class, which handles login actions and assertions for the login page.
"""

from utils.logger import console_logger, LogLevel
from playwright.sync_api import Page
from src.pages.basepage import BasePage
from src.pages.loginpage.locators import LoginPageLocators

logger = console_logger(name="BasePage", level=LogLevel.DEBUG)

class LoginPage(BasePage):
    """
    Page object for the login page.
    """
    # ARRANGE ----------------------------------------
    def __init__(self, page: Page) -> None:
        """Initialize the LoginPage with Playwright Page object."""
        super().__init__(page)
        self._username = self.get_page_locator_by_id(LoginPageLocators.username)
        self._password = self.get_page_locator_by_id(LoginPageLocators.password)

    # ACT ----------------------------------------
    def log_in(self, username: str, password: str) -> None:
        """Perform login action using provided username and password."""
        login_button = self.get_page_locator_by_id(LoginPageLocators.login_button)

        self.navigate_to()
        logger.info(msg=f"Log in with username: '{username}', and password: '{password}'")
        self.fill_page_locator(self._username, username)
        self.fill_page_locator(self._password, password)
        self.click_page_locator(login_button)

    # ASSERT -------------------------------------
    def expect_title_to_have_text(self, text: str) -> None:
        """Assert that the page title contains the specified text."""
        page_locator_title = self.get_page_locator_by_text(text)
        self.expect_page_locator_to_be_visible(page_locator_title)

    def expect_login_page_to_be_visible(self) -> None:
        """Assert that the login page elements are visible."""
        self.expect_page_locator_to_be_visible(self._username)
        self.expect_page_locator_to_be_visible(self._password)

    def expect_error_message(self, error_message: str) -> None:
        """Assert that the error message is visible and contains the expected text."""
        error_message_container = self.get_page_locator_by_selector(
            LoginPageLocators.error_message_container)

        self.expect_page_locator_to_be_visible(error_message_container)
        self.expect_page_locator_to_contain_text(error_message_container, error_message)
