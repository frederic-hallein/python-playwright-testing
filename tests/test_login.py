import pytest



from playwright.sync_api import expect

@pytest.mark.parametrize("user_name", ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user", "error_user", "visual_user"])
def test_log_in(login_page, user_name) -> None:
    password = "secret_sauce"
    login_page.log_in(user_name, password)
    # expect(page).to_have_title("Automation Practice - Ultimate QA")
