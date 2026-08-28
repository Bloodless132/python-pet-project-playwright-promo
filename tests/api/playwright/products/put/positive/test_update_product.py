import allure

from src.framework.api.clients.product_client import ProductClient
from src.framework.api.lib.helper_playwright import check_response_contains, check_response_status
from src.framework.api.test_data.product_data import build_product_payload

def test_update_product(product_client: ProductClient):
    payload = build_product_payload()
    response = product_client.update_product(1, payload)

    with allure.step("Verify response status"):
        check_response_status(response, 200)

    with allure.step("Verify updated product data"):
        check_response_contains(response,"title",payload["title"])
        check_response_contains(response,"description",payload["description"])
        check_response_contains(response,"price",payload["price"])
