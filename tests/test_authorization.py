from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators

class TestAuthorization:

    # проверяем авторизацию через кнопку "Войти в аккаунт"
    def test_auth_button_from_home(self, driver):

        # открываем стартовую страницу
        driver.get("https://stellarburgers.nomoreparties.site")

        # нажали на кнопку "Войти в аккаунт"
        driver.find_element(*Locators.LOGIN_IN_ACCOUNT_BUTTON).click()
        # ожидание страницы авторизации
        WebDriverWait(driver, 2000).until(
            expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON))

        # проверям, что открылась страница авторизации
        current_url = driver.current_url
        assert '/login' in current_url

    # проверяем авторизацию через кнопку «Личный кабинет»
    def test_auth_button_from_personal_account(self, driver):

        # открываем стартовую страницу
        driver.get("https://stellarburgers.nomoreparties.site")

        # нажали на кнопку "Личный кабинет"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        # ожидание страницы ЛК
        WebDriverWait(driver, 30).until(
            expected_conditions.presence_of_element_located(Locators.PERSONAL_ACCOUNT_FIELD_LOGIN))

        # проверям, что открылась страница авторизации
        current_url = driver.current_url
        assert '/login' in current_url

    # проверяем авторизацию через кнопку в форме регистрации
    def test_auth_button_from_register(self, driver):

        # открыли страницу регистрации
        driver.get("https://stellarburgers.nomoreparties.site/register")

        # нажимаем кнопку "Войти" для ранее зарегистрировванных пользователей
        driver.find_element(*Locators.LOGIN_BUTTON_FOR_OLD_PERSON).click()
        # ожидание страницы
        WebDriverWait(driver, 2000).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON))

        # проверям, что открылась страница авторизации
        current_url = driver.current_url
        assert '/login' in current_url

    # проверяем авторизацию через кнопку в форме восстановления пароля
    def test_auth_button_from_restore_password(self, driver):

        # открываем страницу авторизации
        driver.get("https://stellarburgers.nomoreparties.site/login")

        # нажимаем кнопку "Восстановить пароль"
        driver.find_element(*Locators.RESTORE_PASSWORD_BUTTON).click()

        # на открывшейся форме нажимаем кнопку "Войти"
        driver.find_element(*Locators.LOGIN_BUTTON_IN_RESTORE_PASSWORD).click()

        # проверям, что открылась страница восстановления пароля
        current_url = driver.current_url
        assert '/login' in current_url
