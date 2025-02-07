from playwright.sync_api import Page

from src.pages.basepage import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)