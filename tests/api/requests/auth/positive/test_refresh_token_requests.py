import allure

from src.framework.api.clients.requests_auth_client import RequestsAuthClient
from src.framework.api.lib.helper_requests import check_fields_present, check_response_status, check_response_contains
from variables import EMILYS_CORRECT_CREDENTIALS, EMILYS_USER_NAME


def test_refresh_token_requests(requests_auth_client: RequestsAuthClient):
    login_response = requests_auth_client.login(EMILYS_CORRECT_CREDENTIALS)
    refresh_token = login_response.json()["refreshToken"]

    refresh_response = requests_auth_client.refresh_token(refresh_token)

    with allure.step("Verify response status"):
        check_response_status(refresh_response, 200)

    with allure.step("Verify refreshed tokens present"):
        check_fields_present(refresh_response, ["accessToken", "refreshToken"])

    with allure.step("Login with new accessToken"):
        access_token = refresh_response.json()["accessToken"]
        get_authenticated_user_response = requests_auth_client.get_auth_user(access_token)

        check_response_status(get_authenticated_user_response, 200)
        check_response_contains(get_authenticated_user_response, "username", EMILYS_USER_NAME)