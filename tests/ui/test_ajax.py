from playwright.sync_api import Page,expect
from src.framework.ui.pages.ajax_page import AjaxPage


def test_ajax_data(page: Page):
    ajax_page = AjaxPage(page)
    ajax_page.open()
    ajax_page.expect_spinner_hidden()
    ajax_page.click_ajax_request_button()
    ajax_page.expect_spinner_visible()
    ajax_page.expect_ajax_data_banner_hidden()
    ajax_page.expect_ajax_data_banner_visible()
