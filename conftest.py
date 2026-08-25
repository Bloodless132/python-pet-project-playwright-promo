import pytest
from playwright.sync_api import Page, Playwright, expect, APIRequestContext
from src.framework.api.clients.product_client import ProductClient


@pytest.fixture
def page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch()
    page = browser.new_page()

    yield page

    browser.close()


def pytest_configure():
    # Global timeout for expect assertions
    expect.set_options(timeout=20000)


@pytest.fixture
def api_request_context(playwright: Playwright) -> APIRequestContext:
    request_context = playwright.request.new_context(
        base_url="https://dummyjson.com/"
    )
    yield request_context
    request_context.dispose()

@pytest.fixture
def product_client(api_request_context: APIRequestContext) -> ProductClient:
    return ProductClient(api_request_context)
