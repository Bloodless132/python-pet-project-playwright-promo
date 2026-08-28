import json
import logging
from typing import Any

import allure
import requests
from requests import Response


logger = logging.getLogger(__name__)


class RequestsApiClient:

    def __init__(self, base_url: str):
        self._base_url = base_url.rstrip("/")
        self._session = requests.Session()

    def get(self, endpoint: str, **kwargs: Any) -> Response:
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs: Any) -> Response:
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs: Any) -> Response:
        return self._request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs: Any) -> Response:
        return self._request("DELETE", endpoint, **kwargs)



    def _request(self, method: str, endpoint: str, **kwargs: Any) -> Response:
        url = f"{self._base_url}/{endpoint.lstrip('/')}"
        logger.info("%s %s", method, url)
        if "json" in kwargs:
            logger.info("Request body: %s", kwargs["json"])
            allure.attach(
                json.dumps(kwargs["json"], indent=2),
                name="Request body",
                attachment_type=allure.attachment_type.JSON,
            )
        response = self._session.request(method, url, **kwargs)
        logger.info("Response status: %s", response.status_code)
        allure.attach(
            f"{method} {url}\nStatus: {response.status_code}",
            name="Request details",
            attachment_type=allure.attachment_type.TEXT,
        )
        try:
            response_body = response.json()
            logger.info("Response body: %s", response_body)
            allure.attach(
                json.dumps(response_body, indent=2),
                name="Response body",
                attachment_type=allure.attachment_type.JSON,
            )
        except ValueError:
            logger.info("Response body: %s", response.text)
            allure.attach(
                response.text,
                name="Response body",
                attachment_type=allure.attachment_type.TEXT,
            )
        return response

    def close(self) -> None:
        self._session.close()