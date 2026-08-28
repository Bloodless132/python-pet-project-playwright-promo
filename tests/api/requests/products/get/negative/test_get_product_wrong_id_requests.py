import allure

from src.framework.api.clients.requests_product_client import RequestsProductClient
from src.framework.api.lib.helper_requests import check_response_status


def test_get_wrong_id_product_requests(requests_product_client: RequestsProductClient):
    response = requests_product_client.get_product(-1)

    with allure.step("Verify response status"):
        check_response_status(response, 404)