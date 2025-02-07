from playwright.sync_api import Page

from src.pages.login.loginpage import LoginPage

class Navigation(LoginPage):
    def __init__(self, page: Page):
        super().__init__(page)
    
    def go_to_login_page(self):
        # self.open_browser()
        self.browse_to("base")
