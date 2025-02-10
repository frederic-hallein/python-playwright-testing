from playwright.sync_api import Page

from src.pages.basepage import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self._burger_button = self.get_page_locator_by_role("button", "Open Menu")
        self._shopping_cart_button = self.get_page_locator_by_id("shopping_cart_container")
        self._sort_button = self.get_page_locator_by_selector("[class='select_container']")
        self._inventory = self.get_page_locator_by_selector("[class='inventory_container']")
        self._logout_button = self.get_page_locator_by_id("logout_sidebar_link")

    # ACTIONS ----------------------------------------
    def log_out(self) -> None:
        self.click_page_locator(self._burger_button)
        self.click_page_locator(self._logout_button)

    # ASSERTIONS -------------------------------------
    def expect_home_page_to_be_visible(self) -> None:
        self.expect_page_locator_to_be_visible(self._burger_button)
        self.expect_page_locator_to_be_visible(self._shopping_cart_button)
        self.expect_page_locator_to_be_visible(self._sort_button)