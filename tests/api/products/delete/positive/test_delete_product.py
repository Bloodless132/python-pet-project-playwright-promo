import allure

from src.framework.api.clients.product_client import ProductClient
from src.framework.api.lib.helper import check_response_status,check_fields_present,check_response_contains


def test_delete_product(product_client: ProductClient):
    response = product_client.delete_product(1)

    with allure.step("Verify response status"):
        check_response_status(response,200)


    with allure.step("Verify if fields present"):
        check_fields_present(response,["title"])
        check_response_contains(response, "id", 1)
        check_response_contains(response,"title","Essence Mascara Lash Princess")
