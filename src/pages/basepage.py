from utils.helper import yaml_loader

from playwright.sync_api import Page, Locator, expect


from utils.logger import console_logger, LogLevel

logger = console_logger(name="BasePage", level=LogLevel.DEBUG)

class BasePage:
    def __init__(self, page: Page) -> None:
        self._page = page
        self._urls = yaml_loader("res/urls.yaml")

    # PAGE LOCATORS ----------------------------------------------------
    def get_page_locator_by_selector(self, selector: str) -> Locator:
        """ get page locator by selector, i.e. XPATH or CSS """
        return self._page.locator(selector) # TODO: extend with hastext
    
    def get_page_locators_by_selector(self, selector: str) -> Locator:
        """ get page locator by selector, i.e. XPATH or CSS """
        return self._page.locator(selector).all() # TODO: extend with hastext

    def get_page_locator_by_id(self, id: str) -> Locator:
        """ get page locator by attribute name 'id' """
        return self.get_page_locator_by_selector(f"#{id}")

    def get_page_locator_by_role(self, role: tuple[str, str]) -> Locator:
        """ 
        get page locator by explicit and implicit accessibility attributes,
        this includes buttons, checkboxes, headings, links, lists, tables, etc
        """
        return self._page.get_by_role(role[0], name=role[-1])

    def get_page_locator_by_text(self, text: str) -> Locator:
        """ get page locator by text content """
        return self._page.get_by_text(text)

    def get_page_locator_by_label(self, label: str) -> Locator:
        """ get page loactor by a form control by associated label's text """
        return self._page.get_by_label(label)

    # ACTIONS -----------------------------------------
    def navigate_to(self, url: str="base") -> None:
        if url in self._urls: url = self._urls[url]
        logger.info(msg=f"Navigating to url: {url}")
        self._page.goto(url)

    def pause_browser(self) -> None:
        logger.info(msg=f"Browser paused.")
        self._page.pause()

    def click_page_locator(self, page_locator: Locator) -> None:
        logger.info(msg=f"Clicked page locator: {page_locator}")
        page_locator.click()

    def fill_page_locator(self, page_locator: Locator, text: str) -> None:
        logger.info(msg=f"Filled page locator: {page_locator}")
        page_locator.fill(text)

    def select_option_from_dropdown(self, dropdown: Locator, option: str) -> None:
        logger.info(msg=f"Selected option '{option}' from dropdown {dropdown}")
        dropdown.select_option(option)

    def get_text_content(self, page_locator: Locator) -> str:
        return page_locator.text_content()
    
    def get_list_text_content(self, page_locators: list[Locator]) -> list[str]:
        text = []
        for page_locator in page_locators:
            text.append(self.get_text_content(page_locator))
        return text
    
    # ASSERTIONS -----------------------------------------------------
    # TODO : edit asserion messages to account for longer messages
    def expect_page_locator_to_be_visible(self, page_locator: Locator) -> None:
        expect(page_locator).to_be_visible()

    def expect_page_locator_to_contain_text(self, page_locator: Locator, text: str) -> None:
        actual = self.get_text_content(page_locator)
        expect(page_locator).to_contain_text(text)

    def expect_page_locator_to_have_text(self, page_locator: Locator, text: str) -> None:
        actual = self.get_text_content(page_locator)
        expect(page_locator).to_have_text(text)
