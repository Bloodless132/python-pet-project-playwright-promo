import allure
from playwright.sync_api import APIResponse

from src.framework.api.models.product import ProductPayload
from src.framework.api.playwright_api_client import PlaywrightApiClient


class ProductClient:

    def __init__(self, api_client: PlaywrightApiClient):
        self._api_client = api_client

    @allure.step("Get product with id: {product_id}")
    def get_product(self, product_id: int) -> APIResponse:
        return self._api_client.get(f"products/{product_id}")

    @allure.step("Create product")
    def create_product(self, payload: ProductPayload) -> APIResponse:
        return self._api_client.post("products/add", data=payload)

    @allure.step("Update product with id: {product_id}")
    def update_product(self, product_id: int, payload: ProductPayload) -> APIResponse:
        return self._api_client.put(f"products/{product_id}", data=payload)

    @allure.step("Delete product with id: {product_id}")
    def delete_product(self, product_id: int) -> APIResponse:
        return self._api_client.delete(f"products/{product_id}")