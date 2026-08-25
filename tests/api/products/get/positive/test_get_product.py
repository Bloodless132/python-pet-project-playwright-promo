from src.framework.api.clients.product_client import ProductClient


def test_get_product(product_client: ProductClient):

    response = product_client.get_product(1)

    assert response.status == 200

    response_body = response.json()

    assert response_body["id"] == 1
    assert "title" in response_body
    assert "price" in response_body
