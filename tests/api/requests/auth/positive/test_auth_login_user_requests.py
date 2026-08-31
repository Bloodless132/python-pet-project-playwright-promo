import allure

from src.framework.api.clients.requests_auth_client import RequestsAuthClient
from src.framework.api.lib.helper_requests import check_response_contains, check_response_status
from variables import EMILYS_CORRECT_CREDENTIALS


def test_auth_login_user_requests(requests_auth_client: RequestsAuthClient):
    response = requests_auth_client.login(EMILYS_CORRECT_CREDENTIALS)

    with allure.step("Verify response status"):
        check_response_status(response, 200)

    with allure.step("Verify logged user"):
        check_response_contains(response, "username", "emilys")