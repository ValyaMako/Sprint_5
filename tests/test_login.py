from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from conftest import driver, email, register_user


class TestLogin:
    # Проверяем вход через кнопку "Ввойти в аккаунт"
    def test_sign_in_by_button_login(self, driver, email, register_user):
        driver.find_element(*Locators.A_LOGO).click()  # Открыли главную страницу, кликнув на логотип в шапке страницы
        driver.find_element(*Locators.BUTTON_LOGIN).click()  # Нажали кнопку "Ввойти в аккаунт"
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(register_user)  # В поле "Email" ввели почту
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys("qwerty123")   # В поле "Пароль" в вели "qwerty123"
        driver.find_element(*Locators.BUTTON_INTER).click()    # Нажимаем кнопку "Войти"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.BUTTON_CHECKOUT)))   # Ожидаем появления кнопки "Оформить заказ" на главной старнице
        assert driver.find_element(*Locators.BUTTON_CHECKOUT).text == 'Оформить заказ'  # Проверяем, что текст ожидаемой кнопки "Оформить заказ"

    # Проверяем вход через кнопку "Личный кабинет"
    def test_sign_in_by_button_account(self, driver, email, register_user):
        driver.find_element(*Locators.A_LOGO).click()  # Открыли главную страницу, кликнув на логотип в шапке страницы
        driver.find_element(*Locators.BUTTON_ACCOUNT).click()  # Нажали кнопку "Личный кабинет"
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(register_user)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys("qwerty123")
        driver.find_element(*Locators.BUTTON_INTER).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.BUTTON_CHECKOUT)))
        assert driver.find_element(*Locators.BUTTON_CHECKOUT).text == 'Оформить заказ'

    # Проверяем вход через кнопку в форме регистрации
    def test_sign_in_by_button_sing_in_registration_form(self, driver, email, register_user):
        driver.find_element(*Locators.A_LOGO).click()  # Открыли главную страницу, кликнув на логотип в шапке страницы
        driver.find_element(*Locators.BUTTON_LOGIN).click()  # Нажимаем кнопку "Войти в аккаунт"
        driver.find_element(*Locators.A_TO_REGISTER).click()  # Нажимаем ссылку "Зарегистрироваться"
        driver.find_element(*Locators.A_INTER).click()  # Нажимаем ссылку "Войти" в форме регистрации
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(register_user)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys("qwerty123")
        driver.find_element(*Locators.BUTTON_INTER).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.BUTTON_CHECKOUT)))
        assert driver.find_element(*Locators.BUTTON_CHECKOUT).text == 'Оформить заказ'

    # Проверяем вход через кнопку в в форме восстановления пароля.
    def test_sign_in_by_button_in_password_recovery_form(self, driver, email, register_user):
        driver.find_element(*Locators.A_LOGO).click()  # Открыли главную страницу, кликнув на логотип в шапке страницы
        driver.find_element(*Locators.BUTTON_LOGIN).click()  # Нажимаем кнопку "Войти в аккаунт"
        driver.find_element(*Locators.A_RECOVERY_PASSWORD).click()  # Нажимаем ссылку "Восстановить пароль" в форме регистрации
        driver.find_element(*Locators.A_INTER).click()  # Нажимаем ссылку "Войти" в форме восстановления пароля
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(register_user)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys("qwerty123")
        driver.find_element(*Locators.BUTTON_INTER).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.BUTTON_CHECKOUT)))
        assert driver.find_element(*Locators.BUTTON_CHECKOUT).text == 'Оформить заказ'