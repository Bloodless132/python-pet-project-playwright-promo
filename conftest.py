import pytest

from src.framework.api.api_client import ApiClient
from src.framework.api.clients.requests_product_client import RequestsProductClient
from playwright.sync_api import Playwright, expect, APIRequestContext
from src.framework.api.clients.product_client import ProductClient
from variables import DUMMY_JSON_BASE_URL





def pytest_configure():
    # Global timeout for expect assertions
    expect.set_options(timeout=20000)


@pytest.fixture
def api_request_context(playwright: Playwright) -> APIRequestContext:
    request_context = playwright.request.new_context(
        base_url=DUMMY_JSON_BASE_URL
    )
    yield request_context
    request_context.dispose()

@pytest.fixture
def product_client(api_request_context: APIRequestContext) -> ProductClient:
    return ProductClient(api_request_context)

import allure
import pytest
from playwright.sync_api import Page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if isinstance(page, Page):
            screenshot = page.screenshot(full_page=True)

            allure.attach(
                screenshot,
                name="Failure screenshot",
                attachment_type=allure.attachment_type.PNG,
            )


@pytest.fixture
def requests_api_client():
    client = ApiClient(DUMMY_JSON_BASE_URL)
    yield client
    client.close()


@pytest.fixture
def requests_product_client(requests_api_client: ApiClient) -> RequestsProductClient:
    return RequestsProductClient(requests_api_client)