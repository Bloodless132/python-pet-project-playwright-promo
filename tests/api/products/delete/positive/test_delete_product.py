from src.framework.api.clients.product_client import ProductClient


def test_delete_product(product_client: ProductClient):
    response = product_client.delete_product(1)
    assert response.status == 200

    response_body = response.json()
    assert response_body["id"] == 1
    assert response_body["title"] == 'Essence Mascara Lash Princess'
