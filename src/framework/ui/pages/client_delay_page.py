from playwright.sync_api import Page,expect
from src.framework.ui.pages.variables import URL_CLIENT_DELAY
from src.framework.ui.pages.base_page import BasePage

class ClientDelayPage(BasePage):


    def __init__(self, page: Page):
        super().__init__(page, URL_CLIENT_DELAY)
        self.client_side_logic_button = page.get_by_role(
            "button",
            name="Button Triggering Client Side Logic"
        )
        self.client_side_data_banner = page.get_by_text("Data calculated on the client side.")
        self.spinner = page.locator("#spinner")



    def click_client_side_logic_button(self):
        self.client_side_logic_button.click()

    def expect_spinner_visible(self):
        expect(self.spinner).to_be_visible()

    def expect_spinner_hidden(self):
        expect(self.spinner).to_be_hidden()

    def expect_client_side_data_banner_visible(self):
        expect(self.client_side_data_banner).to_be_visible()

    def expect_client_side_data_banner_hidden(self):
        expect(self.client_side_data_banner).to_be_hidden()