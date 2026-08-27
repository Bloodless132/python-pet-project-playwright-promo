from playwright.sync_api import Page
from variables import URL_PROGRESS_BAR
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

    def get_progress_bar_value(self) -> int:
        return int(self.progress_bar.get_attribute("aria-valuenow"))

    def wait_until_progress_bar_reaches(self,target: int):
        while self.get_progress_bar_value() < target:
            self.page.wait_for_timeout(25)
