import allure

from src.framework.api.clients.playwright_auth_client import PlaywrightAuthClient
from src.framework.api.lib.helper_playwright import check_response_contains, check_response_status
from variables import EMILYS_CORRECT_CREDENTIALS


def test_get_authenticated_user(playwright_auth_client: PlaywrightAuthClient):
    login_response = playwright_auth_client.login(EMILYS_CORRECT_CREDENTIALS)
    access_token = login_response.json()["accessToken"]

    response = playwright_auth_client.get_auth_user(access_token)

    with allure.step("Verify response status"):
        check_response_status(response, 200)

    with allure.step("Verify authenticated user"):
        check_response_contains(response, "username", "emilys")