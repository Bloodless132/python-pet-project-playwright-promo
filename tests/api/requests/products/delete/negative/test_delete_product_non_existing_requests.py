import allure

from src.framework.api.clients.requests_product_client import RequestsProductClient
from src.framework.api.lib.helper_requests import check_response_status


def test_delete_product_non_existing_requests(requests_product_client: RequestsProductClient):
    response = requests_product_client.delete_product(-1)

    with allure.step("Verify response status"):
        check_response_status(response, 404)