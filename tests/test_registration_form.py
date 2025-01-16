from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from conftest import driver, email

class TestRegistrationForm:
    # Проверяем успешную регистарцию
    def test_successful_registration(self, driver, email):
        driver.find_element(*Locators.BUTTON_LOGIN).click()  # Нажимаем кнопку "Войти в аккаунт" на главной странице
        driver.find_element(*Locators.A_TO_REGISTER).click()    # Нажимаем ссылку "Зарегистрироваться"
        driver.find_element(*Locators.INPUT_NAME).send_keys("Валентина")   # В поле "Имя" вводим "Валентина"
        driver.find_element(*Locators.INPUT_EMAIL_R).send_keys(email)   # В поле "Email" вводим почту
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys("qwerty123")   # В поле "Пароль" вводим "qwerty123"
        driver.find_element(*Locators.BUTTON_TO_REGISTER).click()    # Нажимаем кнопку "Зврегистрироваться"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.WORD_LOGIN)))  # Ждём появления элемента "Вход"
        assert "login" in driver.current_url  # Проверяем, что открывшаяся страница содержит в url "login"

    # Проверяем появление сообщения об ошибке при вводе некорректного пароля
    def test_error_incorrect_short_password(self, driver, email):
        driver.find_element(*Locators.BUTTON_LOGIN).click()   # Нажимаем кнопку "Войти в аккаунт" на главной странице
        driver.find_element(*Locators.A_TO_REGISTER).click()   # Нажимаем ссылку "Зарегистрироваться"
        driver.find_element(*Locators.INPUT_NAME).send_keys("Валентина")   # В поле "Имя" вводим "Валентина"
        driver.find_element(*Locators.INPUT_EMAIL_R).send_keys(email)   # В поле "Email" вводим почту
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys("qwert")  # В поле "Пароль" вводим "qwert"
        driver.find_element(*Locators.BUTTON_TO_REGISTER).click()   # Нажимаем кнопку "Зврегистрироваться"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.ERROR_PASSWORD)))   # Ждём появления сообщения о ошибке
        assert driver.find_element(*Locators.ERROR_PASSWORD).text == 'Некорректный пароль'   # Проверяем, что текст ошибки "Некорректный пароль"