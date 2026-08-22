from playwright.sync_api import Page,expect
from src.framework.ui.pages.variables import URL_TEXT_INPUT
from src.framework.ui.pages.base_page import BasePage

class TextInputPage(BasePage):


    def __init__(self, page: Page):
        super().__init__(page, URL_TEXT_INPUT)
        self.textbox = page.get_by_placeholder("MyButton")
        self.update_button = page.locator("#updatingButton")


    def click_update_button(self):
        self.update_button.click()

    def fill_textbox(self, input_text: str):
        self.textbox.fill(input_text)

    def expect_textbox_contains_text(self, expected_text: str):
        expect(self.textbox).to_have_value(expected_text)

    def expect_update_button_contains_text(self, expected_text: str):
        expect(self.update_button).to_contain_text(expected_text)