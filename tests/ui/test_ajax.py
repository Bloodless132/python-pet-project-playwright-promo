from playwright.sync_api import Page


def test_ajax_data(page: Page):
    page.goto("http://www.uitestingplayground.com/ajax")

    page.get_by_role("button", name="Button Triggering AJAX Request").click()

    spinner = page.locator("#spinner")
    assert spinner.is_visible() , "Spinner is not visible after button click"

    ajax_request_data = page.get_by_text("Data loaded with AJAX Get request.")
    ajax_request_data.wait_for()  # Wait for AJAX data to be uploaded on the page

    assert ajax_request_data.is_visible() # There is depricated auto-wait functionality