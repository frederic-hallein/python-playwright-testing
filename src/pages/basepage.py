
import yaml

from playwright.sync_api import Page, Locator, expect

from src.logger import console_logger, LogLevel

c_logger = console_logger(name="BasePage", level=LogLevel.DEBUG)

class BasePage:
    def __init__(self, page: Page) -> None:
        self._page = page
        self._urls = yaml.load(open("res/urls.yaml"), Loader=yaml.FullLoader)["urls"]

    # PAGE LOCATORS ----------------------------------------------------
    def get_page_locator_by_selector(self, selector: str) -> Locator:
        """ get page locator by selector, i.e. XPATH or CSS """
        return self._page.locator(selector) # TODO: extend with hastext

    def get_page_locator_by_id(self, id: str) -> Locator:
        """ get page locator by attribute name 'id' """
        return self.get_page_locator_by_selector(f"#{id}")

    def get_page_locator_by_role(self, role: str, name: str) -> Locator:
        """ 
        get page locator by explicit and implicit accessibility attributes,
        this includes buttons, checkboxes, headings, links, lists, tables, etc
        """
        return self._page.get_by_role(role, name=name)

    def get_page_locator_by_text(self, text: str, exact: bool=False) -> Locator:
        """ get page locator by text content """
        return self._page.get_by_text(text, exact)

    def get_page_locator_by_label(self, label: str, exact: bool=False) -> Locator:
        """ get page loactor by a form control by associated label's text """
        return self._page.get_by_label(label, exact)

    # ACTIONS -----------------------------------------
    def navigate_to(self, url: str="base") -> None:
        if url in self._urls: url = self._urls[url]
        c_logger.info(msg=f"Navigating to '{url}'.")
        self._page.goto(url)

    def pause_browser(self) -> None:
        c_logger.info(msg=f"Browser paused.")
        self._page.pause()

    def click_page_locator(self, page_locator: Locator) -> None:
        page_locator.click()

    def fill_page_locator(self, page_locator: Locator, text: str) -> None:
        page_locator.fill(text)

    # ASSERTIONS -----------------------------------------------------
    def expect_correct_title(self, title: str) -> None:
        expect(self._page, f"Expected following title to be visible: {title}").to_have_title(title)

    def expect_page_locator_to_be_visible(self, page_locator: Locator) -> None:
        expect(page_locator, f"Expected following locator to be visible: {page_locator}").to_be_visible()

    def expect_page_locator_to_contain_text(self, page_locator: Locator, text: str) -> None:
        actual = page_locator.text_content()
        expect(page_locator, f"Expected text '{text}', but got '{actual}' instead.").to_contain_text(text)

