from playwright.sync_api import Page,expect
from variables import URL_SCROLL_BAR
from src.framework.ui.pages.base_page import BasePage

class ScrollBarPage(BasePage):


    def __init__(self, page: Page):
        super().__init__(page, URL_SCROLL_BAR)

        self.hiding_button = page.get_by_role("button", name="Hiding Button")


    def click_hiding_button(self):
        self.hiding_button.click()


    def expect_hiding_button_in_viewport(self):
        expect(self.hiding_button).to_be_in_viewport()
