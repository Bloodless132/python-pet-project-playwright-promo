from playwright.sync_api import Page,expect
from src.framework.ui.pages.variables import URL_PROGRESS_BAR
from src.framework.ui.pages.base_page import BasePage

class ProgressBarPage(BasePage):


    def __init__(self, page: Page):
        super().__init__(page, URL_PROGRESS_BAR)
        self.start_button = page.get_by_role(
            "button",
            name="Start"
        )
        self.stop_button = page.get_by_role(
            "button",
            name="Stop"
        )
        self.progress_bar = page.locator("#progressBar")


    def click_start_button(self):
        self.start_button.click()

    def click_stop_button(self):
        self.stop_button.click()

    def expect_progress_bar_contains_value(self, expected_value: str):
        expect(self.progress_bar).to_have_text(f"{expected_value}%")
