import allure
from playwright.sync_api import APIRequestContext, APIResponse


class PlaywrightAuthClient:

    def __init__(self, request_context: APIRequestContext):
        self._request_context = request_context

    @allure.step("Login user: {credentials}")
    def login(self, credentials: dict) -> APIResponse:
        return self._request_context.post(
            "auth/login",
            data=credentials
        )

    @allure.step("Get authenticated user")
    def get_auth_user(self, access_token: str) -> APIResponse:
        return self._request_context.get(
            "auth/me",
            headers={"Authorization": f"Bearer {access_token}"}
        )

    @allure.step("Refresh auth token")
    def refresh_token(self,refresh_token: str) -> APIResponse:
        return self._request_context.post("auth/refresh",data={"refreshToken": refresh_token})
