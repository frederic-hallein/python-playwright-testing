from playwright.sync_api import Page

from src.pages.basepage import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def log_in(self, username: str, password: str):
        self.get_element_by_id("user-name").fill(username)
        self.get_element_by_id("password").fill(password)
        self.get_element_by_id("login-button").click()
        self.pause_browser()
