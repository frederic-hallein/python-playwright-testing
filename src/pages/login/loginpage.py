from src import Page

class LoginPage(Page):
    def __init__(self):
        super().__init__()

    def check_current_page(self):
        pass

    def log_in(self, username: str, password: str):
        self.get_element_by_id("user-name").fill(username)
        self.get_element_by_id("password").fill(password)

