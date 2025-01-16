import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import random

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    yield driver

    driver.quit()

@pytest.fixture(scope="function")
def email():
    return f'Valya_Makovetskaya_17{random.randint(100, 999)}@gmail.com'


@pytest.fixture(scope="function")
def register_user(driver, email):
    driver.find_element(*Locators.BUTTON_LOGIN).click()
    driver.find_element(*Locators.A_TO_REGISTER).click()
    driver.find_element(*Locators.INPUT_NAME).send_keys("Валентина")
    driver.find_element(*Locators.INPUT_EMAIL_R).send_keys(email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys("qwerty123")
    driver.find_element(*Locators.BUTTON_TO_REGISTER).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.WORD_LOGIN)))
    return email

@pytest.fixture(scope="function")
def logged_user(driver, email, register_user):
    driver.find_element(*Locators.A_LOGO).click()
    driver.find_element(*Locators.BUTTON_ACCOUNT).click()
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(register_user)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys("qwerty123")
    driver.find_element(*Locators.BUTTON_INTER).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((Locators.BUTTON_CHECKOUT)))
    return email



