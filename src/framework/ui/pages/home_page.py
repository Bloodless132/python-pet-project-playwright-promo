from playwright.sync_api import Page,expect
from src.framework.ui.pages.variables import URL_HOME
from src.framework.ui.pages.base_page import BasePage

class HomePage(BasePage):


    def __init__(self, page: Page):
        super().__init__(page, URL_HOME)




    def expect_title(self, expected_title: str):
        expect(self.page).to_have_title(expected_title)
