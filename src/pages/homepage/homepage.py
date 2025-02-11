from playwright.sync_api import Page

from src.pages.basepage import BasePage

from src.pages.homepage.locators import Locators

class HomePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self._burger_button = self.get_page_locator_by_role(Locators.burger_button)
        
    # ACTIONS ----------------------------------------
    def log_out(self) -> None:
        logout_button = self.get_page_locator_by_id(Locators.logout_button)

        self.click_page_locator(self._burger_button)
        self.click_page_locator(logout_button)

    # ASSERTIONS -------------------------------------
    def expect_home_page_to_be_visible(self) -> None:
        shopping_cart_button = self.get_page_locator_by_id(Locators.shopping_cart_button)
        sort_button = self.get_page_locator_by_selector(Locators.sort_button)
        inventory = self.get_page_locator_by_selector(Locators.inventory)

        self.expect_page_locator_to_be_visible(self._burger_button)
        self.expect_page_locator_to_be_visible(shopping_cart_button)
        self.expect_page_locator_to_be_visible(sort_button)
        self.expect_page_locator_to_be_visible(inventory)