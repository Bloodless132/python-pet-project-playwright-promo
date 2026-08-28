import allure

from src.framework.api.clients.requests_product_client import RequestsProductClient
from src.framework.api.lib.helper_requests import check_response_status
from src.framework.api.test_data.product_data import build_product_payload


def test_update_non_existing_product_requests(requests_product_client: RequestsProductClient):
    payload = build_product_payload()
    response = requests_product_client.update_product(999999, payload)

    with allure.step("Verify response status"):
        check_response_status(response, 404)