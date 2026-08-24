from playwright.sync_api import Playwright


def test_post_product(playwright: Playwright):
    request_context = playwright.request.new_context(
        base_url="https://dummyjson.com/"
    )

    payload = {
        "title": "BMW pencil",
        "description": "Nice BMW pencil",
        "price": 9.99
    }
    response = request_context.post("products/add", data=payload)


    assert response.status == 201

    response_body = response.json()

    assert "title" in response_body
    assert "description" in response_body
    assert "price" in response_body
    assert "id" in response_body

    assert response_body["title"] == payload["title"]
    assert response_body["description"] == payload["description"]
    assert response_body["price"] == payload["price"]

    request_context.dispose()
