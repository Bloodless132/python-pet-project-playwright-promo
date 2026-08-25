from src.framework.ui.lib.helper import random_string
from playwright.sync_api import Page
from src.framework.ui.pages.text_input_page import TextInputPage


def test_text_input(page: Page):
    text_input_page = TextInputPage(page)

    text_input_page.open()

    text_input_data = random_string()

    text_input_page.fill_textbox(text_input_data)
    text_input_page.expect_textbox_contains_text(text_input_data)

    text_input_page.click_update_button()

    text_input_page.expect_update_button_contains_text(text_input_data)



