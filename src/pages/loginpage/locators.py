"""
Locators for elements on the login page.
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class LoginPageLocators:
    """
    Data class containing locator definitions for the login page.
    """
    username: str = "user-name"
    password: str = "password"
    login_button: str = "login-button"
    error_message_container: str = "[class='error-message-container error']"
