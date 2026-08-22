from playwright.sync_api import Page
from src.framework.ui.pages.progress_bar_page import ProgressBarPage


def test_progress_bar(page: Page):
    progress_bar_page = ProgressBarPage(page)
    progress_bar_page.open()

    progress_bar_page.click_start_button()

    progress_bar_page.expect_progress_bar_contains_value("75")
    progress_bar_page.click_stop_button()

    progress_bar_page.expect_progress_bar_contains_value("75")
