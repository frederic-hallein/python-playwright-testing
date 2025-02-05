from src import Page

class LoginPage(Page):

    def check_current_page(self):
        pass

    def log_in(self, user_name: str, password: str):
        self.open_browser()
        self.browse_to("base")
        # TODO : input text

