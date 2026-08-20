from playwright.sync_api import Page,expect
from src.framework.ui.pages.variables import URL_DYNAMIC_ID
from src.framework.ui.pages.base_page import BasePage


class DynamicIdPage(BasePage):


    def __init__(self, page: Page):
        self.page = page
        super().__init__(page, URL_DYNAMIC_ID)
        self.dynamic_id_button = page.get_by_role(
            "button",
            name="Button with Dynamic ID"
        )

    def get_button_dynamic_id(self) -> str | None:
        return self.dynamic_id_button.get_attribute("id")

    def click_dynamic_id_button(self):
        self.dynamic_id_button.click()

    def expect_dynamic_id_button_visible(self):
        expect(self.dynamic_id_button).to_be_visible()