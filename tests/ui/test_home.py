from playwright.sync_api import Page,expect


def test_home_page(page: Page):
    page.goto("http://www.uitestingplayground.com/home")

    assert page.title() == "UI Test Automation Playground"
