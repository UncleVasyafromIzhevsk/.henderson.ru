import re
from playwright.sync_api import Page, expect


def log(msg):
    print(msg.text)


def test_example(page: Page) -> None:
    page.on("console", log)
    page.goto("https://henderson.ru/hlogin")
    page.goto("https://henderson.ru/hlogin?tk=7a81d46944bf62d2")
    page.get_by_role("textbox").first.click()
    page.get_by_role("textbox").first.fill("d")
    page.get_by_role("textbox").first.click()
    page.get_by_role("textbox").first.click()
    # page.get_by_role("textbox").first.fill("drin@gmail.com")
    # page.locator("input[name=\"password\"]").click()
    # page.locator("input[name=\"password\"]").fill("12987y6t5")
    page.get_by_role("button", name="Войти").click()
    page.get_by_text("Забыли пароль?", exact=True).click()
    page.get_by_role("textbox").nth(2).click()
    page.get_by_role("textbox").nth(2).fill("tetst79@mail.ru")
    page.locator("#sendForgotpassword").click()