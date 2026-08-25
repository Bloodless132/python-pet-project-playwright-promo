import allure

from src.framework.api.clients.product_client import ProductClient
from src.framework.api.lib.helper import check_response_status


def test_get_non_existing_product(product_client: ProductClient):
    response = product_client.get_product(1000000)

    with allure.step("Verify response status"):
        check_response_status(response,404)