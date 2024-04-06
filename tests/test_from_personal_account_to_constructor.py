from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators

class TestFromPersonalAccountToConstructor:

    def test_from_personal_account_to_constructor(self, driver, user):

        # открыли страницу регистрации
        driver.get("https://stellarburgers.nomoreparties.site/register")

        # ожидание страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.REGISTRATION_FORM))

        # ввели имя
        driver.find_element(*Locators.REGISTRATION_NAME_FIELD).send_keys(user.name)
        # ввели логин (почта)
        email = user.email
        driver.find_element(*Locators.REGISTRATION_EMAIL_FIELD).send_keys(email)
        # ввели пароль
        driver.find_element(*Locators.REGISTRATION_PASSWORD_FIELD).send_keys("QWASZX12")
        # нажали кнопку "Зарегистрироваться"
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        # ожидание страницы авторизации
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON))
        # ввели логин (почта)
        driver.find_element(*Locators.AUTH_EMAIL_FIELD).send_keys(email)
        # ввели пароль
        driver.find_element(*Locators.AUTH_PASSWORD_FIELD).send_keys("QWASZX12")
        # нажали кнопку "Войти"
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        # ожидание страницы после авторизации
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON))
        # переходим в ЛК по кнопке "Личный кабинет"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        # ожидание страницы ЛК
        WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located(Locators.PERSONAL_ACCOUNT_FIELD_LOGIN))

        # нажали на кнопку "Конструктор"
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        # ожидание загрузки страницы
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(Locators.COLLECT_BURGER))

        # прокрутить до конца страницы с бургерами
        page_burgers = driver.find_element(*Locators.COLLECT_BURGER)
        driver.execute_script("arguments[0].scrollIntoView();", page_burgers)

        assert 'Сыр с астероидной плесенью' in page_burgers.text

    def test_from_personal_account_to_logo(self, driver, user):

        # открыли страницу регистрации
        driver.get("https://stellarburgers.nomoreparties.site/register")

        # ожидание страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.REGISTRATION_FORM))

        # ввели имя
        driver.find_element(*Locators.REGISTRATION_NAME_FIELD).send_keys(user.name)
        # ввели логин (почта)
        email = user.email
        driver.find_element(*Locators.REGISTRATION_EMAIL_FIELD).send_keys(email)
        # ввели пароль
        driver.find_element(*Locators.REGISTRATION_PASSWORD_FIELD).send_keys("QWASZX12")
        # нажали кнопку "Зарегистрироваться"
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        # ожидание страницы авторизации
        WebDriverWait(driver, 2000).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON))
        # ввели логин (почта)
        driver.find_element(*Locators.AUTH_EMAIL_FIELD).send_keys(email)
        # ввели пароль
        driver.find_element(*Locators.AUTH_PASSWORD_FIELD).send_keys("QWASZX12")
        # нажали кнопку "Войти"
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        # ожидание страницы после авторизации
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON))
        # переходим в ЛК по кнопке "Личный кабинет"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        # ожидание страницы ЛК
        WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located(Locators.PERSONAL_ACCOUNT_FIELD_LOGIN))

        # нажали на кнопку логотипа Stellar Burgers
        driver.find_element(*Locators.LOGO_BUTTON).click()
        # ожидание загрузки страницы
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(
            (Locators.COLLECT_BURGER)))

        # прокрутить до конца страницы "Соберите бургер"
        page_burgers = driver.find_element(*Locators.COLLECT_BURGER)
        driver.execute_script("arguments[0].scrollIntoView();", page_burgers)

        assert 'Сыр с астероидной плесенью' in page_burgers.text
