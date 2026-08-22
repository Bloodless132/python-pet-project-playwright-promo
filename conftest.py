import pytest
from playwright.sync_api import Page, Playwright, expect


@pytest.fixture
def page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch()
    page = browser.new_page()

    yield page

    browser.close()


def pytest_configure():
    # Global timeout for expect assertions
    expect.set_options(timeout=20000)
