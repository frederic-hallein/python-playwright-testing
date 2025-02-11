from playwright.sync_api import Page

from src.pages.basepage import BasePage

from src.pages.loginpage.locators import Locators

class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self._username = self.get_page_locator_by_id(Locators.username)
        self._password = self.get_page_locator_by_id(Locators.password)

    # ACTIONS ----------------------------------------
    def log_in(self, username: str, password: str) -> None:
        login_button = self.get_page_locator_by_id(Locators.login_button)

        self.fill_page_locator(self._username, username)
        self.fill_page_locator(self._password, password)
        self.click_page_locator(login_button)

    # ASSERTIONS -------------------------------------
    def expect_login_page_to_be_visible(self) -> None:
        self.expect_page_locator_to_be_visible(self._username)
        self.expect_page_locator_to_be_visible(self._password)

    def expect_error_message(self, error_message: str) -> None:
        error_message_container = self.get_page_locator_by_selector(Locators.error_message_container)

        self.expect_page_locator_to_be_visible(error_message_container)
        self.expect_page_locator_to_contain_text(error_message_container, error_message)