import allure

from src.framework.api.clients.requests_auth_client import RequestsAuthClient
from src.framework.api.lib.helper_requests import check_response_status,check_response_contains
from variables import INVALID_CREDENTIALS_MESSAGE


def test_auth_login_wrong_password_requests(requests_auth_client: RequestsAuthClient):
    response = requests_auth_client.login("emilys", "wrong_password")

    with allure.step("Verify response status"):
        check_response_status(response, 400)
        check_response_contains(response, "message", INVALID_CREDENTIALS_MESSAGE)