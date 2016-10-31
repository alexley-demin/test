from main_page import MainPage
from Page import PageLogin
from unittest import TestCase
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class OttripTest(TestCase):
    def setUp(self):
        """
        Предусловие:
        зайти на сайт www.onetwotrip.com
        нажать "личный кабинет"
        """
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        page = MainPage(self.driver)
        page.open("http://www.onetwotrip.com/ru")
        page.top_panel.click_button_personal_area()

    def tearDown(self):
        self.driver.quit()

    def test_forgot_password_non_existent_email(self):
        """
        Тест-кейс "Проверка вывода сообщения об ошибке при вводе несуществующего email в форме "забыли пароль""
        Шаги:
        1. Нажать "забыли пароль"
        2. В поле "Электронная почта" ввести несуществующий email
        3. Нажать кнопку "Получить пароль"
        Ожидание:
        Вывод сообщения об ошибке "Пользователя с таким email не существует" в браузере.
        """
        page_auth = PageLogin(self.driver)
        page_auth.auth_form.forgot_password("lllll@mail.ru")

        error = page_auth.auth_form.get_error_message_incorrect_email()
        self.assertIn("Пользователя с таким email не существует", error)

    def test_forgot_password_correct_email(self):
        """
        Тест-кейс "Проверка вывода сообщения об отправке нового пароля на указанный email в форме "забыли пароль""
        Шаги:
        1.Нажать "забыли пароль"
        2.В поле "Электронная почта" ввести зарегистрированный на onetwotrip email
        3.Нажать кнопку "Получить пароль"
        Ожидание:
        Вывод сообщения об отправке нового пароля на указанный email.
        """
        page_auth = PageLogin(self.driver)
        page_auth.auth_form.forgot_password("ld040994@mail.ru")

        message = page_auth.auth_form.message_sending_new_pass_is_displayed()
        self.assertTrue(message)

    def test_auth_incorrect_login(self):
        """
        Тест-кейс "Проверка вывода сообщения об ошибке при вводе неверного логина в форме авторизации"
        Шаги:
        1.В поле "Электронная почта" вести почту незарегистрированную на onetwotrip
        2.В поле "Пароль" ввести пароль
        3.Нажать кнопку "Войти"
        Ожидание:
        Вывод сообщения "Неправильный пароль или почта"
        """
        page_auth = PageLogin(self.driver)
        page_auth.auth_form.authorization("l040994@mail.ru","040994alex")

        error = page_auth.auth_form.get_error_message_incorrect_login()
        self.assertIn("Неправильный пароль или почта", error)

    def test_auth_correct(self):
        """
        Тест-кейс "Проверка ввода верного логина и пароля в форме авторизации"
        Шаги:
        1.В поле "Электронная почта" вести почту зарегистрированную на onetwotrip
        2.В поле "Пароль" ввести верный пароль
        3.Нажать кнопку "Войти"
        Ожидание:
        Успешная авторизация (название кнопки личный кабинет заменяется на email адрес)
        """
        page_auth = PageLogin(self.driver)
        page_auth.auth_form.authorization("ld040994@mail.ru","040994alex")

        profile = MainPage(self.driver).top_panel.get_user_name()
        self.assertEqual(profile, "ld040994@mail.ru")

    def test_auth_facebook(self):
        """
        Тест-кейс "Проверка ввода верного логина и пароля в форме авторизации"
        Шаги:
        1.Нажать на иконку Facebook
        2.В новом окне ввести логин и пароль от аккаунта Facebook
        3.Нажать кнопку "Войти"
        Ожидание:
        Успешная авторизация (название кнопки "личный кабинет" заменяется название профиля)
        """
        page_auth = PageLogin(self.driver)
        page_auth.auth_form.auth_facebook("alexld45@mail.ru","040994alex")

        profile = MainPage(self.driver).top_panel.get_user_name()
        self.assertEqual(profile, "Алексей Демин")


if __name__ == '__main__':
    unittest.main()
