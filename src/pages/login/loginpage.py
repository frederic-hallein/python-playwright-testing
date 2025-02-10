from playwright.sync_api import Page

from src.pages.basepage import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self._username_locator = self.get_page_locator_by_id("user-name")
        self._password_locator = self.get_page_locator_by_id("password")
        self._login_button = self.get_page_locator_by_id("login-button")
        self._error_message_container = self.get_page_locator_by_selector("[class='error-message-container error']")

    # ACTIONS ----------------------------------------
    def log_in(self, username: str, password: str) -> None:
        self.fill_page_locator(self._username_locator, username)
        self.fill_page_locator(self._password_locator, password)
        self.click_page_locator(self._login_button)

    # ASSERTIONS -------------------------------------
    def expect_login_page_to_be_visible(self) -> None:
        self.expect_page_locator_to_be_visible(self._username_locator)
        self.expect_page_locator_to_be_visible(self._password_locator)

    def expect_error_message(self, error_message: str) -> None:
        self.expect_page_locator_to_be_visible(self._error_message_container)
        self.expect_page_locator_to_contain_text(self._error_message_container, error_message)