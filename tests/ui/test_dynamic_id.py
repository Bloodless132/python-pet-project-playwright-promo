from playwright.sync_api import Page
from src.framework.ui.pages.dynamic_id_page import DynamicIdPage


def test_dynamic_id_button(page: Page):
    dynamic_id_page = DynamicIdPage(page)
    dynamic_id_page.open()

    id_button_before_reload = dynamic_id_page.get_button_dynamic_id()
    dynamic_id_page.click_dynamic_id_button()
    dynamic_id_page.expect_dynamic_id_button_visible()

    dynamic_id_page.reload()  # Reload page and later verify the same button but changed id

    id_button_after_reload = dynamic_id_page.get_button_dynamic_id()
    dynamic_id_page.click_dynamic_id_button()
    dynamic_id_page.expect_dynamic_id_button_visible()
    assert id_button_before_reload != id_button_after_reload

