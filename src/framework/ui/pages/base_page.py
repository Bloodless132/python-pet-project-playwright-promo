from playwright.sync_api import Page


class BasePage:


    def __init__(self, page: Page, url: str):
        self.page = page
        self.url = url
        self.default_timeout = 20000

    def open(self):
        self.page.goto(self.url)

    def reload(self):
        self.page.reload()
