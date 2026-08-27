from playwright.sync_api import Page,expect
from variables import URL_AJAX
from src.framework.ui.pages.base_page import BasePage

class AjaxPage(BasePage):


    def __init__(self, page: Page):
        super().__init__(page, URL_AJAX)
        self.ajax_request_button = page.get_by_role(
            "button",
            name="Button Triggering AJAX Request"
        )
        self.ajax_data_banner = page.get_by_text("Data loaded with AJAX Get request.")
        self.spinner = page.locator("#spinner")



    def click_ajax_request_button(self):
        self.ajax_request_button.click()

    def expect_spinner_visible(self):
        expect(self.spinner).to_be_visible()

    def expect_spinner_hidden(self):
        expect(self.spinner).to_be_hidden()

    def expect_ajax_data_banner_visible(self):
        expect(self.ajax_data_banner).to_be_visible()

    def expect_ajax_data_banner_hidden(self):
        expect(self.ajax_data_banner).to_be_hidden()