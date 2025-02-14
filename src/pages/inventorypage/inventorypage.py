from utils.custom_except import expect_equality

from playwright.sync_api import Page
from src.pages.basepage import BasePage
from src.pages.inventorypage.locators import Locators

class InventoryPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self._burger_button = self.get_page_locator_by_role(Locators.burger_button)
        self._valid_sort_options = {
            "name"         :"Name (A to Z)",
            "name_reverse" :"Name (Z to A)",
            "price"        :"Price (low to high)",
            "price_reverse":"Price (high to low)"
        }
        
    # ACTIONS ----------------------------------------
    def log_out(self) -> None:
        logout_button = self.get_page_locator_by_id(Locators.logout_button)

        self.click_page_locator(self._burger_button)
        self.click_page_locator(logout_button)

    def sort_inventory_by(self, sort: str) -> None:
        if sort not in self._valid_sort_options.values():
            raise AssertionError(f"Sorting by '{sort}' is not a valid option.")

        product_sort_dropdown = self.get_page_locator_by_selector(Locators.product_sort_dropdown)
        self.select_option_from_dropdown(product_sort_dropdown, sort)

    # ASSERTIONS -------------------------------------
    def expect_inventory_page_to_be_visible(self) -> None:
        shopping_cart_button = self.get_page_locator_by_id(Locators.shopping_cart_button)
        product_sort_dropdown = self.get_page_locator_by_selector(Locators.product_sort_dropdown)
        inventory = self.get_page_locator_by_selector(Locators.inventory)

        self.expect_page_locator_to_be_visible(self._burger_button)
        self.expect_page_locator_to_be_visible(shopping_cart_button)
        self.expect_page_locator_to_be_visible(product_sort_dropdown)
        self.expect_page_locator_to_be_visible(inventory)

    def expect_inventory_to_be_sorted_by(self, sort: str) -> None:
        inventory_item_names = self.get_list_text_content(
            self.get_page_locators_by_selector(Locators.inventory_item_name)
        )
        inventory_item_prices = self.get_list_text_content(
            self.get_page_locators_by_selector(Locators.inventory_item_price)
        )

        if sort == self._valid_sort_options.get("name"):
            inventory_item_names_sorted = sorted(inventory_item_names)
            expect_equality(inventory_item_names, inventory_item_names_sorted)
        elif sort == self._valid_sort_options.get("name_reverse"):
            inventory_item_names_sorted = sorted(inventory_item_names, reverse=True)
            expect_equality(inventory_item_names, inventory_item_names_sorted)
        elif sort == self._valid_sort_options.get("price"):
            inventory_item_prices_sorted = sorted(inventory_item_prices, 
                                                  key=lambda x: float(x.replace('$', '')))
            expect_equality(inventory_item_prices, inventory_item_prices_sorted)
        elif sort == self._valid_sort_options.get("price_reverse"):
            inventory_item_prices_sorted = sorted(inventory_item_prices, 
                                                  key=lambda x: float(x.replace('$', '')), reverse=True)
            expect_equality(inventory_item_prices, inventory_item_prices_sorted)
        else:
            raise AssertionError(f"Sorting by '{sort}' is not a valid option.")

