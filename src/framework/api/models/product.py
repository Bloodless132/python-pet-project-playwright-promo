from typing import TypedDict


class ProductPayload(TypedDict):
    title: str
    description: str
    price: float