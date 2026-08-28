import allure

from src.framework.api.clients.product_client import ProductClient
from src.framework.api.test_data.product_data import build_product_payload
from src.framework.api.lib.helper_playwright import check_response_contains,check_response_status


def test_post_product(product_client: ProductClient):
    payload = build_product_payload()
    response = product_client.create_product(payload)

    with allure.step("Verify response status"):
        check_response_status(response, 201)

    with allure.step("Verify created product data"):
        check_response_contains(response, "title",payload["title"])
        check_response_contains(response,"description",payload["description"])
        check_response_contains(response,"price",payload["price"])
