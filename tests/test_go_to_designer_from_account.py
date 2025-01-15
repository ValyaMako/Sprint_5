from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from conftest import driver, email, register_user, logged_user

class TestToDesignerFromAccount:
    # Проверяем переход из личного кабинета в конструктор по нажатию на кнопку "Конструктор"
    def test_to_designer_from_account_by_button_designer(self, driver, email, register_user, logged_user):
        driver.find_element(*Locators.BUTTON_ACCOUNT).click()  # Нажали кнопку "Личный кабинет"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.A_PROFILE))) # Ждём загрузки страницы профиля
        driver.find_element(*Locators.BUTTON_DESIGNER).click()  # Нажимаем кнопку "Конструктор"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.BUTTON_CHECKOUT)))  # Ждём загрузки главной страницы
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    # Проверяем переход из личного кабинета в конструктор по нажатию на логотип Stellar Burgers
    def test_to_designer_from_account_by_logo(self, driver, email, register_user, logged_user):
        driver.find_element(*Locators.BUTTON_ACCOUNT).click()  # Нажали кнопку "Личный кабинет"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.A_PROFILE)))   # Ждём загрузки страницы профиля
        driver.find_element(*Locators.A_LOGO).click()  # Нажимаем логотип в шапке страницы
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.BUTTON_CHECKOUT)))   # Ждём загрузки главной страницы
        assert driver.current_url =='https://stellarburgers.nomoreparties.site/'
