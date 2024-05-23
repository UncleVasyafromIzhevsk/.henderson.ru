import datetime
import time

from playwright.sync_api import Page, expect
from loguru import logger

logger.add("file.log", format="{extra[email]} {extra[message]} {message}")


def test_henderson(page: Page) -> None:
    """Заходим на страницу и перебираем имена и хосты почты"""
    page.goto("https://henderson.ru/hlogin")
    page.goto("https://henderson.ru/hlogin?tk=8dc46c8fbb065a91")
    page.get_by_role("button", name="Войти").click()
    page.get_by_text("Забыли пароль?", exact=True).click()
    page.get_by_role("textbox").nth(2).click()

    def check_and_record():
        """Ввод данных и запись в лог"""
        page.get_by_role("textbox").nth(2).fill(email)
        page.locator("#sendForgotpassword").click()
        try:
            page.get_by_text("Неправильный email.").click()
            warning = "Неправильный email."
        except Exception as e:
            print(e)
        try:
            page.get_by_text(
                "Введенный логин не зарегистрирован. Пожалуйста, воспользуйтесь формой регистрации"
            ).click()
            warning = (
                    "Введенный логин не зарегистрирован. " +
                    "Пожалуйста, воспользуйтесь формой регистрации")
        except Exception as e:
            print(e)

        warning_info = ("Сообщение сайта: " + warning + "\n")

        context_logger = logger.bind(email=email_info, message=warning_info)
        context_logger.info(datetime.datetime.now())

    special_signs = '#$%&‘*+—/=?^_`{|}~.'
    i = 0
    # Проверка с символами и цифрами
    for signs in special_signs:
        email_first_name = 'vasy'
        email_last_name = 'ivaniv'
        email_host = '@gmail.com'
        email = (email_first_name + str(i) + signs + email_last_name + email_host)
        email_info = ("EMAIL: " + email + "\n")

        check_and_record()

        i += 1
    # Проверка с символами
    for signs in special_signs:
        email_first_name = 'vasy'
        email_last_name = 'ivaniv'
        email_host = '@gmail.com'
        email = (email_first_name + signs + email_last_name + email_host)
        email_info = ("EMAIL: " + email + "\n")

        check_and_record()
    # Проверка с цифрами
    for signs in special_signs:
        email_first_name = 'vasy'
        email_last_name = 'ivaniv'
        email_host = '@gmail.com'
        email = (email_first_name + str(i) + email_last_name + email_host)
        email_info = ("EMAIL: " + email + "\n")

        check_and_record()

        i += 1
    # Проверка хоста
    host = 'gm-il.'
    email_host = ''
    while len(email_host) <= 80:
        email_name = 'ivaniv'
        email_host += host
        email = (email_name + '@' + email_host + 'com')
        email_info = ("EMAIL: " + email + "\n")

        check_and_record()
    # Проверка общей длины почты
    email_host = '@gmail.com'
    name = 'inanovIvanIvanich'
    email_name = ''
    email = ''
    i = 0
    while len(email) <= 360:
        email_name += (name + str(i))
        email = (email_name + email_host)
        email_info = ("EMAIL: " + email + "\n")

        check_and_record()

        i += 1


