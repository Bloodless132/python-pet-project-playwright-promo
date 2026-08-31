import allure

from src.framework.api.clients.requests_auth_client import RequestsAuthClient
from src.framework.api.lib.helper_requests import check_response_contains, check_response_status
from variables import EMILYS_CORRECT_CREDENTIALS


def test_get_authenticated_user_requests(requests_auth_client: RequestsAuthClient):
    login_response = requests_auth_client.login(EMILYS_CORRECT_CREDENTIALS)
    access_token = login_response.json()["accessToken"]

    response = requests_auth_client.get_auth_user(access_token)

    with allure.step("Verify response status"):
        check_response_status(response, 200)

    with allure.step("Verify authenticated user"):
        check_response_contains(response, "username", "emilys")