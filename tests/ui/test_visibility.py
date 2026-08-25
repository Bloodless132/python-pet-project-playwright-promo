from playwright.sync_api import Page
from src.framework.ui.pages.visibility_page import VisibilityPage


def test_visibility(page: Page):
    visibility_page = VisibilityPage(page)
    visibility_page.open()

    visibility_page.expect_hide_button_visible()
    visibility_page.expect_removed_button_visible()
    visibility_page.expect_zero_width_button_visible()
    visibility_page.expect_overlapped_button_visible()
    visibility_page.expect_opacity_zero_button_visible()
    visibility_page.expect_visibility_hidden_button_visible()
    visibility_page.expect_display_none_button_visible()
    visibility_page.expect_offscreen_button_visible()

    visibility_page.click_hide_button()

    visibility_page.expect_hide_button_visible()
    visibility_page.expect_removed_button_hidden()
    visibility_page.expect_zero_width_button_hidden()
    visibility_page.expect_overlapped_button_not_clickable()
    visibility_page.expect_opacity_zero_button_have_css_zero_opacity()
    visibility_page.click_opacity_zero_button()
    visibility_page.expect_visibility_hidden_button_hidden()
    visibility_page.expect_display_none_button_visible()
    visibility_page.expect_offscreen_button_not_in_viewport()


