"""
Base page object providing common actions and assertions for Playwright page objects.
"""

from utils.logger import console_logger, LogLevel
from utils.helper import yaml_loader
from playwright.sync_api import Page, Locator, expect

logger = console_logger(name="BasePage", level=LogLevel.DEBUG)

class BasePage:
    """
    Common base class for all page objects, with shared Playwright actions and assertions.
    """
    # ARRANGE ----------------------------------------
    def __init__(self, page: Page) -> None:
        self._page = page
        self._urls = yaml_loader("res/urls.yaml")

    # PAGE LOCATORS ----------------------------------------------------
    def get_page_locator_by_selector(self, selector: str, has_text: str = None) -> Locator:
        """ get page locator by selector, i.e. XPATH or CSS """
        # return self._page.locator(selector)
        if has_text:
            return self._page.locator(selector, has_text=has_text)
        return self._page.locator(selector)

    def get_all_page_locators_by_selector(self, selector: str, has_text: str = None) -> Locator:
        """ get all page locator by selector, i.e. XPATH or CSS """
        # return self._page.locator(selector).all()
        if has_text:
            return self._page.locator(selector, has_text=has_text).all()
        return self._page.locator(selector).all()

    def get_page_locator_by_id(self, element_id: str) -> Locator:
        """ get page locator by attribute name 'id' """
        return self.get_page_locator_by_selector(f"#{element_id}")

    def get_page_locator_by_role(self, role: tuple[str, str]) -> Locator:
        """
        get page locator by explicit and implicit accessibility attributes,
        this includes buttons, checkboxes, headings, links, lists, tables, etc
        """
        return self._page.get_by_role(role[0], name=role[-1])

    def get_page_locator_by_text(self, text: str) -> Locator:
        """ get page locator by text content """
        return self._page.get_by_text(text)

    def get_all_page_locators_by_text(self, text: str) -> Locator:
        """ get all page locator by text content """
        return self._page.get_by_text(text).all()

    def get_page_locator_by_label(self, label: str) -> Locator:
        """ get page loactor by a form control by associated label's text """
        return self._page.get_by_label(label)

    def get_child_page_locator(self, parent_page_locator: Locator,
                               child_selector: Locator) -> Locator:
        """Return a child locator from a parent locator using the given selector."""
        return parent_page_locator.locator(child_selector)

    # ACT -----------------------------------------
    def navigate_to(self, url: str="base") -> None:
        """Navigate to the specified URL or the base URL."""
        if url in self._urls:
            url = self._urls[url]
        logger.info(msg=f"Navigating to url: {url}")
        self._page.goto(url)

    def pause_browser(self) -> None:
        """Pause the browser execution for debugging purposes."""
        logger.info(msg="Browser paused.")
        self._page.pause()

    def click_page_locator(self, page_locator: Locator) -> None:
        """Click the specified page locator."""
        logger.info(msg=f"Clicked page locator: {page_locator}")
        page_locator.click()

    def fill_page_locator(self, page_locator: Locator, text: str) -> None:
        """Fill the specified page locator with the given text."""
        logger.info(msg=f"Filled page locator: {page_locator}")
        page_locator.fill(text)

    def select_option_from_dropdown(self, dropdown: Locator, option: str) -> None:
        """Select the given option from the specified dropdown locator."""
        logger.info(msg=f"Selected option '{option}' from dropdown {dropdown}")
        dropdown.select_option(option)

    def get_text_content(self, page_locator: Locator) -> str:
        """Return the text content of the given page locator."""
        return page_locator.text_content()

    def get_list_text_content(self, page_locators: list[Locator]) -> list[str]:
        """Return a list of text contents for the given list of page locators."""
        text = []
        for page_locator in page_locators:
            text.append(self.get_text_content(page_locator))
        return text

    # ASSERT -----------------------------------------------------
    def expect_page_locator_to_be_visible(self, page_locator: Locator) -> None:
        """Assert that the given page locator is visible."""
        expect(page_locator).to_be_visible()

    def expect_page_locator_to_contain_text(self, page_locator: Locator, text: str) -> None:
        """Assert that the given page locator contains the specified text."""
        expect(page_locator).to_contain_text(text)

    def expect_page_locator_to_have_text(self, page_locator: Locator, text: str) -> None:
        """Assert that the given page locator has the exact specified text."""
        expect(page_locator).to_have_text(text)
