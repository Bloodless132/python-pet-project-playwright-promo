from playwright.sync_api import APIRequestContext, APIResponse
from src.framework.api.models.product import ProductPayload


class ProductClient:

    def __init__(self, request_context: APIRequestContext):
        self._request_context = request_context

    def get_product(self, product_id: int) -> APIResponse:
        return self._request_context.get(
            f"products/{product_id}"
        )

    def create_product(self, payload: ProductPayload) -> APIResponse:
        return self._request_context.post(
            "products/add",
            data=payload
        )

    def update_product(self,  product_id: int, payload: ProductPayload) -> APIResponse:
        return self._request_context.put(
            f"products/{product_id}",
            data=payload
        )

    def delete_product(self,  product_id: int) -> APIResponse:
        return self._request_context.delete(
            f"products/{product_id}"
        )