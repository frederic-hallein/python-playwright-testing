"""
Locators for elements on the inventory page.
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class InventoryPageLocators:
    """
    Data class containing locator definitions for the inventory page.
    """
    burger_button: tuple = ("button", "Open Menu")
    shopping_cart_button: str = "shopping_cart_container"
    product_sort_dropdown: str = "//*[@class='product_sort_container']"
    inventory: str = "//*[@class='inventory_container']"
    logout_button: str = "logout_sidebar_link"
    inventory_item: str = "//*[@class='inventory_item']"
    inventory_item_name: str = "//*[@class='inventory_item_name ']"
    inventory_item_price: str = "//*[@class='inventory_item_price']"
    add_to_cart_button: str = "Add to cart"
