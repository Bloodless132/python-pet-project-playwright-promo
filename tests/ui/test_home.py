from playwright.sync_api import Page,expect
from src.framework.ui.pages.home_page import HomePage

def test_home_page(page: Page):
    home_page = HomePage(page)

    home_page.open()
    home_page.expect_title("UI Test Automation Playground")
