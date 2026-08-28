import allure

from src.framework.api.clients.product_client import ProductClient
from src.framework.api.lib.helper_playwright import check_response_status,check_fields_present,check_response_contains


def test_delete_product_non_existing(product_client: ProductClient):
    response = product_client.delete_product(-1)

    with allure.step("Verify response status"):
        check_response_status(response,404)
