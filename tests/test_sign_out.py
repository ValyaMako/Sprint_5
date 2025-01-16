from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from conftest import driver, email, register_user, logged_user


class TestSignOut:
    # Проверяем выход по кнопке "Выход" в личном кабинете
    def test_sign_out_by_button_in_personal_account(self, driver, email, register_user, logged_user):
        driver.find_element(*Locators.BUTTON_ACCOUNT).click()   # Кликаем на кнопку "Личный кабинет"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.A_PROFILE)))  # Ожидаем загрузки старницы профиля появлением элементы "Профиль"
        driver.find_element(*Locators.BUTTON_OUT).click()  # Кликаем кнопку "Выход"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.WORD_LOGIN)))   # Ожидаем загрузки страницы входа появлением элемента "Вход"
        assert 'login' in driver.current_url  # Проверяем, что URL содержит "login"
