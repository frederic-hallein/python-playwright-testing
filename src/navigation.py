# from src import Page
from src.pages.login.loginpage import LoginPage

class Navigation(LoginPage):
    def __init__(self):
        super().__init__()
    
    def go_to_login_page(self):
        self.open_browser()
        self.browse_to("base")
