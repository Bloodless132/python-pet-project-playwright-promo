import allure
import random
import string

from requests import Response


def random_string(length: int = 10) -> str:
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


@allure.step("Check response contains field {field_name} == {expected_field_value}")
def check_response_contains(response: Response, field_name: str, expected_field_value):
    if response is not None:
        response_body = response.json()
        actual_field_value = response_body[field_name]

        assert actual_field_value == expected_field_value, (
            f"Wrong actual value for field {field_name}. "
            f"Actual result: {actual_field_value}. "
            f"Expected result: {expected_field_value}"
        )
    else:
        raise AssertionError("Response body is empty")


@allure.step("Check response status is {expected_status_code}")
def check_response_status(response: Response, expected_status_code: int):
    assert response.status_code == expected_status_code, (
        f"Wrong actual status code for response. "
        f"Actual result: {response.status_code}. "
        f"Expected result: {expected_status_code}"
    )


@allure.step("Check response contains fields {expected_fields}")
def check_fields_present(response: Response, expected_fields: list):
    if response is not None:
        response_body = response.json()

        for field in expected_fields:
            assert field in response_body, (
                f"Field '{field}' is not present in response payload."
            )
    else:
        raise AssertionError("Response body is empty")