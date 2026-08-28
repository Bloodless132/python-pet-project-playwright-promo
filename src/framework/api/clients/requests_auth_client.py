import allure
from requests import Response

from src.framework.api.requests_api_client import RequestsApiClient


class RequestsAuthClient:

    def __init__(self, api_client: RequestsApiClient):
        self._api_client = api_client

    @allure.step("Login user: {username}")
    def login(self, username: str, password: str) -> Response:
        return self._api_client.post(
            "auth/login",
            json={"username": username, "password": password}
        )

    @allure.step("Get authenticated user")
    def get_auth_user(self, access_token: str) -> Response:
        return self._api_client.get(
            "auth/me",
            headers={"Authorization": f"Bearer {access_token}"}
        )

    @allure.step("Refresh auth token")
    def refresh_token(self,refresh_token: str) -> Response:
        return self._api_client.post("auth/refresh",json={"refreshToken": refresh_token})