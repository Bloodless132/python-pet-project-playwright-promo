from playwright.sync_api import Playwright

def test_get_product(playwright: Playwright):
    request_context = playwright.request.new_context(
        base_url="https://dummyjson.com/"
    )

    response = request_context.get("products/1")

    assert response.status == 200

    response_body = response.json()

    assert response_body["id"] == 1
    assert "title" in response_body
    assert "price" in response_body

    request_context.dispose()