import logging
import allure
import pytest

from playwright.sync_api import Page

from src.framework.api.clients.playwright_auth_client import PlaywrightAuthClient
from src.framework.api.clients.requests_auth_client import RequestsAuthClient
from src.framework.api.playwright_api_client import PlaywrightApiClient
from src.framework.api.requests_api_client import RequestsApiClient
from src.framework.api.clients.requests_product_client import RequestsProductClient
from playwright.sync_api import Playwright, expect
from src.framework.api.clients.product_client import ProductClient
from variables import DUMMY_JSON_BASE_URL





def pytest_configure():
    # Global timeout for expect assertions
    expect.set_options(timeout=20000)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )


@pytest.fixture
def playwright_api_client(playwright: Playwright) -> PlaywrightApiClient:
    request_context = playwright.request.new_context()
    client = PlaywrightApiClient(request_context, DUMMY_JSON_BASE_URL)
    yield client
    request_context.dispose()

@pytest.fixture
def requests_api_client():
    client = RequestsApiClient(DUMMY_JSON_BASE_URL)
    yield client
    client.close()


@pytest.fixture
def product_client(playwright_api_client: PlaywrightApiClient) -> ProductClient:
    return ProductClient(playwright_api_client)

@pytest.fixture
def requests_product_client(requests_api_client: RequestsApiClient) -> RequestsProductClient:
    return RequestsProductClient(requests_api_client)


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
def playwright_auth_client(playwright_api_client: PlaywrightApiClient) -> PlaywrightAuthClient:
    return PlaywrightAuthClient(playwright_api_client)

@pytest.fixture
def requests_auth_client(requests_api_client: RequestsApiClient) -> RequestsAuthClient:
    return RequestsAuthClient(requests_api_client)
