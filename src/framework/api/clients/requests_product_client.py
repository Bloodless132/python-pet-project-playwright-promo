import allure
from requests import Response

from src.framework.api.requests_api_client import RequestsApiClient
from src.framework.api.models.product import ProductPayload


class RequestsProductClient:

    def __init__(self, api_client: RequestsApiClient):
        self._api_client = api_client

    @allure.step("Get product with id: {product_id}")
    def get_product(self, product_id: int) -> Response:
        return self._api_client.get(f"products/{product_id}")

    @allure.step("Create product")
    def create_product(self, payload: ProductPayload) -> Response:
        return self._api_client.post("products/add", json=payload)

    @allure.step("Update product with id: {product_id}")
    def update_product(self, product_id: int, payload: ProductPayload) -> Response:
        return self._api_client.put(f"products/{product_id}", json=payload)

    @allure.step("Delete product with id: {product_id}")
    def delete_product(self, product_id: int) -> Response:
        return self._api_client.delete(f"products/{product_id}")