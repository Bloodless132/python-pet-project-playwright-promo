import allure

from src.framework.api.clients.playwright_auth_client import PlaywrightAuthClient
from src.framework.api.lib.helper_playwright import check_response_status,check_response_contains
from variables import INVALID_CREDENTIALS_MESSAGE,EMILYS_WRONG_USERNAME_CREDENTIALS


def test_auth_login_wrong_username(playwright_auth_client: PlaywrightAuthClient):
    response = playwright_auth_client.login(EMILYS_WRONG_USERNAME_CREDENTIALS   )

    with allure.step("Verify response status"):
        check_response_status(response, 400)
        check_response_contains(response,"message",INVALID_CREDENTIALS_MESSAGE)