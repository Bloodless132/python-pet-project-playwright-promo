from playwright.sync_api import Page


def test_dynamic_id_button(page: Page):
    page.goto("http://www.uitestingplayground.com/dynamicid")

    button = page.get_by_role("button", name="Button with Dynamic ID")
    id_button_before_reload = button.get_attribute('id')
    button.click()
    assert button.is_visible()

    page.reload()  # Reload page and later verify the same button but changed id

    button = page.get_by_role("button", name="Button with Dynamic ID")
    id_button_after_reload = button.get_attribute('id')
    button.click()
    assert button.is_visible()
    assert id_button_before_reload != id_button_after_reload

