import yaml

from playwright.sync_api import sync_playwright
from playwright.sync_api import Locator

from src.logger import console_logger, LogLevel

c_logger = console_logger(name="page", level=LogLevel.DEBUG)

class Page:
    def __init__(self):
        self.browser = None
        self.context = None
        self.page = None
        self._urls = yaml.load(open("res/urls.yaml"), Loader=yaml.FullLoader)["urls"]
        

    def open_browser(self, browser: str="chromium", headless: bool=False, maximize_window: bool=True):
        c_logger.info(f"Opening browser")
        playwright = sync_playwright().start()

        args = []
        no_viewport = False
        if maximize_window:
            args.append("--start-maximized")
            no_viewport = True

        match browser:
            case "chromium": playwright_browser = playwright.chromium
            case "webkit"  : playwright_browser = playwright.webkit
            case "firefox" : playwright_browser = playwright.firefox
            case _: raise AssertionError(f"Browser '{browser}' is not a valid browser")
        
        self.browser = playwright_browser.launch(headless=headless, args=args)
        self.context = self.browser.new_context(no_viewport=no_viewport)
        self.page = self.context.new_page()


    def browse_to(self, url: str="base"):
        if url in self._urls: url = self._urls[url]
        self.page.goto(url)

    def close_browser(self):
        c_logger.info(f"Closing browser")
        if self.browser:
            self.context.close()
            self.browser.close()
            self.browser = None
            self.browser = None
            self.page = None
        
    def pause_browser(self):
        self.page.pause()

    def get_element_by_selector(self, selector: str):
        return self.page.locator(selector) # TODO: extend with hastext

    def get_element_by_id(self, id: str) -> Locator:
        return self.get_element_by_selector(f"#{id}")

    def get_element_by_role(self, role: str, name: str) -> Locator:
        return self.page.get_by_role(role, name=name)

    def get_by_text(self, text: str, exact: bool=False) -> Locator:
        self.page.get_by_text(text, exact)

    def get_element_by_label(self, label: str, exact: bool=False) -> Locator:
        return self.page.get_by_label(label, exact)

    def get_element_by_placecholder(self, placeholder: str, exact: bool=False) -> Locator:
        return self.page.get_by_placeholder(placeholder, exact)

    def get_by_alt_text(self) -> Locator:
        pass

    def get_by_title(self) -> Locator:
        pass

    def get_by_test_id(self) -> Locator:
        pass