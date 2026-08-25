from src.framework.api.lib.helper import random_string
from src.framework.api.models.product import ProductPayload
import random

def build_product_payload(
        title: str = random_string(),
        description: str = random_string(),
        price: float = random.randint(0, 100),
        **overrides) -> ProductPayload:
    payload = {
        "title": title,
        "description": description,
        "price": price,
    }
    payload.update(overrides)
    return payload
