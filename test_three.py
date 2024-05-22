import re
import time
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://henderson.ru/hlogin")
    page.goto("https://henderson.ru/hlogin?tk=6d555755cbde68a6")
    time.sleep(2)
    page.get_by_text("Забыли пароль?", exact=True).click()
    page.get_by_role("textbox").nth(2).click()
    page.get_by_role("textbox").nth(2).fill("fdgh@gmail.com")
    page.locator("#sendForgotpassword").click()