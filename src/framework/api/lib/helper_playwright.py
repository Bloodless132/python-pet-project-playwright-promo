import allure


import random
import string

from playwright.sync_api import APIResponse

def random_string(length: int = 10) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@allure.step("Check response contains field {field_name} == {expected_field_value}")
def check_response_contains(response: APIResponse, field_name: str, expected_field_value):
    if response:
        response_body = response.json()
        actual_field_value = response_body[field_name]

        assert actual_field_value== expected_field_value, (f"Wrong actual value for field {field_name}."
                                                           f"Actual result: {actual_field_value}"
                                                           f"Expected result: {expected_field_value}")
    else:
        raise AssertionError("Response body is empty")

@allure.step("Check response status is {expected_status_code}")
def check_response_status(response: APIResponse, expected_status_code: int):
        assert response.status == expected_status_code, (f"Wrong actual status code for response. "
                                                           f"Actual result: {response.status} "
                                                           f"Expected result: {expected_status_code}")

@allure.step("Check response contains fields {expected_fields}")
def check_fields_present(response: APIResponse, expected_fields: list):
    if response:
        response_body = response.json()
        for field in expected_fields:
            assert field in response_body, f"Field '{field}' is not present in response payload."
    else:
        raise AssertionError("Response body is empty")

@allure.step("Check responses contains different values for field {fields}")
def check_fields_not_equal_in_responses(response_first: APIResponse, response_second: APIResponse, fields: list):
    if response_first and response_second:
        response_body_1 = response_first.json()
        response_body_2 = response_second.json()
        for field in fields:
            assert response_body_1[field] != response_body_2[field], f"Field '{field}' is the same for both responses."
    else:
        raise AssertionError(f"Some of responses is empty:"
                             f"Response first: {response_first.json()}"
                             f"Response second: {response_second.json()}")