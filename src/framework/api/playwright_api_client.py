import json
import logging
from typing import Any

import allure
from playwright.sync_api import APIRequestContext, APIResponse


logger = logging.getLogger(__name__)


class PlaywrightApiClient:

    def __init__(self, request_context: APIRequestContext, base_url: str):
        self._request_context = request_context
        self._base_url = base_url.rstrip("/")

    def get(self, endpoint: str, **kwargs: Any) -> APIResponse:
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs: Any) -> APIResponse:
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs: Any) -> APIResponse:
        return self._request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs: Any) -> APIResponse:
        return self._request("DELETE", endpoint, **kwargs)

    def _request(self, method: str, endpoint: str, **kwargs: Any) -> APIResponse:
        url = f"{self._base_url}/{endpoint.lstrip('/')}"
        logger.info("%s %s", method, url)

        if "data" in kwargs:
            logger.info("Request body: %s", kwargs["data"])
            allure.attach(json.dumps(kwargs["data"], indent=2), "Request body", allure.attachment_type.JSON)

        response = self._request_context.fetch(url, method=method, **kwargs)

        logger.info("Response status: %s", response.status)
        allure.attach(f"{method} {url}\nStatus: {response.status}", "Request details", allure.attachment_type.TEXT)

        try:
            body = response.json()
            logger.info("Response body: %s", body)
            allure.attach(json.dumps(body, indent=2), "Response body", allure.attachment_type.JSON)
        except ValueError:
            body = response.text()
            logger.info("Response body: %s", body)
            allure.attach(body, "Response body", allure.attachment_type.TEXT)

        return response