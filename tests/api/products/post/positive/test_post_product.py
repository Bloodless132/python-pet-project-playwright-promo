from src.framework.api.clients.product_client import ProductClient
from src.framework.api.test_data.product_data import build_product_payload


def test_post_product(product_client: ProductClient):
    payload = build_product_payload()

    response = product_client.create_product(payload)

    assert response.status == 201

    response_body = response.json()

    assert "id" in response_body
    assert response_body["title"] == payload["title"]
    assert response_body["description"] == payload["description"]
    assert response_body["price"] == payload["price"]

