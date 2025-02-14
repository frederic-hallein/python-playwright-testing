import pytest
import random
from utils.helper import yaml_loader

users = yaml_loader("res/users.yaml").values()
valid_sort_options = ["Name (A to Z)", "Name (Z to A)", "Price (low to high)", "Price (high to low)"]

@pytest.mark.parametrize(("username", "password"), users)
class TestSortingInventory:
    @pytest.mark.sorting
    def test_sorting(self, login_page, username, password, inventory_page) -> None:
        # ACTIONS ----------------------------------------
        login_page.log_in(username, password)
        sort = random.choice(valid_sort_options)
        inventory_page.sort_inventory_by(sort)

        # ASSERTIONS -------------------------------------
        inventory_page.expect_inventory_to_be_sorted_by(sort)