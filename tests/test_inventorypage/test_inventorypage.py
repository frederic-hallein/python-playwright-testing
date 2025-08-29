"""
Tests for the inventory page functionality.
"""

import random
import pytest

from utils.helper import yaml_loader

class TestInventoryPage:
    """
    Test suite for inventory page scenarios.
    """
    @pytest.mark.logout
    def test_log_out(self, login_page, users, inventory_page) -> None:
        """Test logging out from the inventory page."""
        # ARRANGE ------------------------------------
        username = random.choice(users["userName"])
        password = users["password"]

        # ACT ------------------------------------
        login_page.log_in(username, password)
        inventory_page.log_out()

        # ASSERT ------------------------------------
        login_page.expect_login_page_to_be_visible()

    @pytest.mark.sorting
    def test_sorting(self, login_page, users, inventory_page) -> None:
        """Test sorting inventory items by various options."""
        # ARRANGE ------------------------------------
        valid_sort_options = ["Name (A to Z)", "Name (Z to A)",
                              "Price (low to high)", "Price (high to low)"]
        sort = random.choice(valid_sort_options)
        username = random.choice(users["userName"])
        password = users["password"]

        # ACT ----------------------------------------
        login_page.log_in(username, password)
        inventory_page.sort_inventory_by(sort)

        # ASSERT -------------------------------------
        inventory_page.expect_inventory_to_be_sorted_by(sort)

    @pytest.mark.skip(reason="Test not implemented yet")
    @pytest.mark.add_to_cart
    def test_add_to_cart(self, login_page, inventory_page) -> None:
        """Test adding random items to the cart and print their names."""
        # ARRANGE ------------------------------------


        # ACTIONS ----------------------------------------
        login_page.navigate_to("inventory")
        inventory_items = inventory_page.get_all_inventory_items()
        amount = random.randint(1, len(inventory_items))
        random_inventory_items = random.choices(inventory_items, k=amount)
        for inventory_item in random_inventory_items:
            inventory_name = inventory_page.get_inventory_item_name(inventory_item)
            print(inventory_name)

        # ASSERTIONS -------------------------------------

