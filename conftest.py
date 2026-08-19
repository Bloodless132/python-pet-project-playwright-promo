import pytest
from playwright.sync_api import Page, Playwright


@pytest.fixture
def page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch()
    page = browser.new_page()

    yield page

    browser.close()