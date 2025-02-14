import pytest

from utils.helper import yaml_loader

users = yaml_loader("res/users.yaml").values()

class TestLogOut:
    @pytest.mark.logout
    @pytest.mark.parametrize(("username", "password"), users)
    def test_log_out(self, login_page, username, password, inventory_page) -> None:
        # ACTIONS ------------------------------------
        login_page.log_in(username, password)
        inventory_page.log_out()

        # ASSERTIONS ------------------------------------
        login_page.expect_login_page_to_be_visible()