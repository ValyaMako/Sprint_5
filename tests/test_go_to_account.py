from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from conftest import driver, email, register_user, logged_user


class TestToPersonalAccount:
    # Проверяем переход по клику на "Личный кабинет"
    def test_go_to_account(self, driver, email, register_user, logged_user):
        driver.find_element(*Locators.BUTTON_ACCOUNT).click()  # Нажали кнопку "Личный кабинет"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.A_PROFILE)))  # Ждем появления элемента "Профиль" в личном кабинете
        assert 'profile' in driver.current_url  # Проверили, что URL содержит "profile"
