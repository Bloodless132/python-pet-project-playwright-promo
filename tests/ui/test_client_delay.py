from playwright.sync_api import Page

from src.framework.ui.pages.client_delay_page import ClientDelayPage


def test_client_side_delay(page: Page):
    client_delay_page = ClientDelayPage(page)
    client_delay_page.open()
    client_delay_page.expect_spinner_hidden()
    client_delay_page.click_client_side_logic_button()
    client_delay_page.expect_spinner_visible()
    client_delay_page.expect_client_side_data_banner_hidden()
    client_delay_page.expect_client_side_data_banner_visible()