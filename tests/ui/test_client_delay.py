from playwright.sync_api import Page


def test_client_side_delay(page: Page):
    page.goto("http://www.uitestingplayground.com/clientdelay")

    page.get_by_role("button", name="Button Triggering Client Side Logic").click()

    spinner = page.locator("#spinner")
    assert spinner.is_visible() , "Spinner is not visible after button click"

    client_data_calculation = page.get_by_text("Data calculated on the client side.")
    client_data_calculation.wait_for()  # Wait for calculation to be done on the page
    assert client_data_calculation.is_visible() # There is depricated auto-wait functionality