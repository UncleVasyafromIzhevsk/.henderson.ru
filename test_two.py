import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def log(msg):
    print(msg)


def test_two(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.on("console", log)
    page.goto("https://henderson.ru/hlogin")
    page.goto("https://henderson.ru/hlogin?tk=cd695ea014b9522a")
    time.sleep(3)
    page.get_by_role("textbox").first.click()
    # page.get_by_role("textbox").first.fill("dfcz@gmail.com")
    # page.locator("input[name=\"password\"]").click()
    # page.locator("input[name=\"password\"]").fill("1265t564r")
    page.get_by_role("button", name="Войти").click()
    page.get_by_text("Забыли пароль?", exact=True).click()
    page.get_by_role("textbox").nth(2).click()
    page.get_by_role("textbox").nth(2).fill("tetst79@mail.ru")
    page.locator("#sendForgotpassword").click()
    time.sleep(10)

    # ---------------------
    context.close()
    browser.close()


