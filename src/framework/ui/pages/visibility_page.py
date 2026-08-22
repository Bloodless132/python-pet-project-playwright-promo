import pytest
from playwright.sync_api import Page,expect
from src.framework.ui.pages.variables import URL_VISIBILITY
from src.framework.ui.pages.base_page import BasePage
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError


class VisibilityPage(BasePage):


    def __init__(self, page: Page):
        super().__init__(page, URL_VISIBILITY)

        self.hide_button = page.get_by_role("button", name="Hide")
        self.removed_button = page.get_by_role("button", name="Removed")
        self.zero_width_button = page.get_by_role("button",name="Zero Width")
        self.overlapped_button = page.get_by_role("button",name="Overlapped")
        self.opacity_zero_button = page.get_by_role("button",name="Opacity 0")
        self.visibility_hidden_button = page.get_by_role("button",name="Visibility Hidden")
        self.display_none_button = page.get_by_role("button",name="Display None")
        self.offscreen_button = page.get_by_role("button",name="Offscreen")



    def click_hide_button(self):
        self.hide_button.click()


    def expect_hide_button_visible(self):
        expect(self.hide_button).to_be_visible()

    def expect_removed_button_visible(self):
        expect(self.removed_button).to_be_visible()

    def expect_zero_width_button_visible(self):
        expect(self.zero_width_button).to_be_visible()

    def expect_overlapped_button_visible(self):
        expect(self.overlapped_button).to_be_visible()

    def expect_opacity_zero_button_visible(self):
        expect(self.opacity_zero_button).to_be_visible()

    def expect_visibility_hidden_button_visible(self):
        expect(self.visibility_hidden_button).to_be_visible()

    def expect_display_none_button_visible(self):
        expect(self.display_none_button).to_be_visible()

    def expect_offscreen_button_visible(self):
        expect(self.offscreen_button).to_be_visible()


    def expect_removed_button_hidden(self):
        expect(self.removed_button).to_be_hidden()

    def expect_zero_width_button_hidden(self):
        expect(self.zero_width_button).to_be_hidden()

    def expect_opacity_zero_button_have_css_zero_opacity(self):
        expect(self.opacity_zero_button).to_have_css("opacity", "0")

    def click_opacity_zero_button(self):
       self.opacity_zero_button.click()

    def expect_visibility_hidden_button_hidden(self):
        expect(self.visibility_hidden_button).to_be_hidden()

    def expect_display_none_button_hidden(self):
        expect(self.display_none_button).to_be_hidden()

    def expect_offscreen_button_not_in_viewport(self):
        expect(self.offscreen_button).not_to_be_in_viewport()

    def expect_overlapped_button_not_clickable(self):
        with pytest.raises(PlaywrightTimeoutError):
            self.overlapped_button.click(timeout=100)
