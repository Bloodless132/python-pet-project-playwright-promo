from src.framework.api.clients.product_client import ProductClient


def test_get_non_existing_product(product_client: ProductClient):
    response = product_client.get_product(-1)

    assert response.status == 404