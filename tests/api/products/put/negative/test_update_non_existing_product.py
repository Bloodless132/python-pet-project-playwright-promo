from src.framework.api.clients.product_client import ProductClient
from src.framework.api.test_data.product_data import build_product_payload


def test_update_non_existing_product(product_client: ProductClient):
    payload = build_product_payload()
    response = product_client.update_product(999999, payload)
    assert response.status == 404