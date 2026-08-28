import allure

from src.framework.api.clients.playwright_auth_client import PlaywrightAuthClient
from src.framework.api.lib.helper_playwright import check_response_contains, check_response_status
from variables import EMILYS_CORRECT_CREDENTIALS


def test_auth_login_user(playwright_auth_client: PlaywrightAuthClient):
    response = playwright_auth_client.login(EMILYS_CORRECT_CREDENTIALS)

    with allure.step("Verify response status"):
        check_response_status(response, 200)

    with allure.step("Verify logged user"):
        check_response_contains(response, "username", "emilys")