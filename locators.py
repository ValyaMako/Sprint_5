from selenium.webdriver.common.by import By

class Locators:
# Элементы на главной странице
    BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти в аккаунт']")    # Кнопка "Войти в аккаунт"
    BUTTON_ACCOUNT = (By.XPATH, "//a[@href='/account']")               # Ссылка "Личный кабинет"
    A_LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")          # Логотип в шапке страницы
    BUTTON_DESIGNER = (By.CLASS_NAME, "AppHeader_header__link__3D_hX") # Кнопка "Конструктор"
    BUTTON_CHECKOUT = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка "Оформить заказ"

# Элементы формы регистрации
    INPUT_NAME = (By.XPATH, "//fieldset[1]//input")                         # Поле ввода "Имя"
    INPUT_EMAIL_R = (By.XPATH, "//fieldset[2]//input")                      # Поле ввода "Email" в форме регистрации
    INPUT_PASSWORD = (By.XPATH, "//input[@type='password']")                # Поле ввода "Пароль" в форме регистрации/входа
    BUTTON_TO_REGISTER = (By.XPATH, "//button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться" в форме регистрации
    ERROR_PASSWORD = (By.XPATH, "//p[contains(@*, 'error')]")               # Сообщение о некорректном пароле в форме регистрации
    A_INTER = (By.CLASS_NAME, "Auth_link__1fOlj")                           # Ссылка "Войти" в форме регистрации/ восстановления пароля

# Элементы формы входа
    WORD_LOGIN = (By.XPATH, "//h2[text()='Вход']")                       # Слово "Вход" на странице входа
    A_TO_REGISTER = (By.XPATH, "//a[text()='Зарегистрироваться']")       # Ссылка "Зарегистрироваться" на странице входа
    INPUT_EMAIL = (By.XPATH, "//input[@name='name']")                    # Поле ввода "Email" в форме входа
    BUTTON_INTER = (By.XPATH, "//button[text()='Войти']")                # Кнопка "Войти" в форме входа
    A_RECOVERY_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']") # Ссылка "Восстановить пароль"

# Элементы профиля авторизованного пользователя
    A_PROFILE = (By.XPATH, "//a[text()='Профиль']")      # "Профиль" в личном кабинете
    BUTTON_OUT = (By.XPATH, "//button[text()='Выход']")  # Кнопка "Выход" в личном кабинете

# Элементы раздела "Соберите бургер"
    # Кнопки навигации
    BUTTON_ROLLS = (By.XPATH, "//span[text()='Булки']/..")        # Кнопка "Булки"
    BUTTON_SAUCES = (By.XPATH, "//span[text()='Соусы']/..")       # Кнопка "Соусы"
    BUTTON_STUFFINGS = (By.XPATH, "//span[text()='Начинки']/..")  # Кнопка "Начинки"

    # Названия разделов
    SECTION_ROLLS = (By.XPATH, "//h2[text()='Булки']")        # Раздел "Булки"
    SECTION_SAUCES = (By.XPATH, "//h2[text()='Соусы']")       # Раздел "Соусы"
    SECTION_STUFFINGS = (By.XPATH, "//h2[text()='Начинки']")  # Раздел "Начинки"