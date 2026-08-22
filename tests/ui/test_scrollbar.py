from playwright.sync_api import Page,expect
from src.framework.ui.pages.scrollbar_page import ScrollBarPage


def test_scrollbar(page: Page):
    scrollbar_page = ScrollBarPage(page)

    scrollbar_page.open()

    scrollbar_page.click_hiding_button()
    scrollbar_page.expect_hiding_button_in_viewport()
