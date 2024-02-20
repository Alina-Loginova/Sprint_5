from selenium import webdriver
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestAuthorization:

    # проверяем авторизацию через кнопку "Войти в аккуант"
    def test_auth_button_from_home(self):

        # открыли страницу
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        # сначала регистрируем нового пользователя

        # нажали на кнопку "Войти"
        driver.find_element(By.XPATH, ".//section[2]/div/button").click()
        # ожидание страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться")))
        # нажали на кнопку "Зарегистрироваться"
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
        # ожидание страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))

        # ввели имя
        driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("Alina")
        # ввели логин (почта)
        Email = f"alina_loginova_1_{random.randint(100, 999)}@gmail.com"
        driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(Email)
        # ввели пароль
        driver.find_element(By.NAME, "Пароль").send_keys("QWASZX12")
        # нажали кнопку "Зарегистрироваться"
        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()


        # теперь авторизуемся под учеткой созданного пользователя

        # открываем стартовую страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

        # открыли страницу авторизации по кнопке "Войти в аккаунт"
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()

        # ожидание страницы авторизации
        WebDriverWait(driver, 2000).until(
            expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text()='Войти']")))
        # ввели логин (почта)
        driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys(Email)
        # ввели пароль
        driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys("QWASZX12")
        # нажали кнопку "Войти"
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

        # ожидание страницы после авторизации
        WebDriverWait(driver, 2000).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Личный Кабинет")))
        # переходим в ЛК по кнопке "Личный кабинет"
        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        # ожидание страницы ЛК
        WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.NAME, "name")))

        # проверяем, что логин в ЛК совпадает с первоначальным при авторизации
        Element = driver.find_element(By.NAME, "name")
        assert Element.get_attribute('value') == Email

        driver.quit()

    # проверяем авторизацию через кнопку «Личный кабинет»
    def test_auth_button_from_personal_account(self):
        # открыли страницу
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        # сначала регистрируем нового пользователя

        # нажали на кнопку "Войти"
        driver.find_element(By.XPATH, ".//section[2]/div/button").click()
        # ожидание страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться")))
        # нажали на кнопку "Зарегистрироваться"
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
        # ожидание страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))

        # ввели имя
        driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("Alina")
        # ввели логин (почта)
        Email = f"alina_loginova_1_{random.randint(100, 999)}@gmail.com"
        driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(Email)
        # ввели пароль
        driver.find_element(By.NAME, "Пароль").send_keys("QWASZX12")
        # нажали кнопку "Зарегистрироваться"
        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

        # теперь авторизуемся под учеткой созданного пользователя

        # открываем стартовую страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

        # нажимаем на кнопку "Личный кабинет"
        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()

        # ожидание страницы авторизации
        WebDriverWait(driver, 2000).until(
            expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text()='Войти']")))
        # ввели логин (почта)
        driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys(Email)
        # ввели пароль
        driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys("QWASZX12")
        # нажали кнопку "Войти"
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

        # ожидание страницы после авторизации
        WebDriverWait(driver, 2000).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Личный Кабинет")))
        # переходим в ЛК по кнопке "Личный кабинет"
        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        # ожидание страницы ЛК
        WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.NAME, "name")))

        # проверяем, что логин в ЛК совпадает с первоначальным при авторизации
        Element = driver.find_element(By.NAME, "name")
        assert Element.get_attribute('value') == Email

        driver.quit()

    # проверяем авторизацию через кнопку в форме регистрации
    def test_auth_button_from_register(self):
        # открыли страницу
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        # сначала регистрируем нового пользователя

        # нажали на кнопку "Войти"
        driver.find_element(By.XPATH, ".//section[2]/div/button").click()
        # ожидание страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться")))
        # нажали на кнопку "Зарегистрироваться"
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
        # ожидание страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))

        # ввели имя
        driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("Alina")
        # ввели логин (почта)
        Email = f"alina_loginova_1_{random.randint(100, 999)}@gmail.com"
        driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(Email)
        # ввели пароль
        driver.find_element(By.NAME, "Пароль").send_keys("QWASZX12")
        # нажали кнопку "Зарегистрироваться"
        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()


        # теперь авторизуемся под учеткой созданного пользователя

        # открываем страницу регистрации
        driver.get("https://stellarburgers.nomoreparties.site/register")

        # нажимаем кнопку "Войти" для ранее зарегистрировванных пользователей
        driver.find_element(By.XPATH, ".//*[@id='root']/div/main/div/div/p/a").click()

        # ожидание страницы авторизации
        WebDriverWait(driver, 2000).until(
            expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text()='Войти']")))
        # ввели логин (почта)
        driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys(Email)
        # ввели пароль
        driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys("QWASZX12")
        # нажали кнопку "Войти"
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

        # ожидание страницы после авторизации
        WebDriverWait(driver, 2000).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Личный Кабинет")))
        # переходим в ЛК по кнопке "Личный кабинет"
        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        # ожидание страницы ЛК
        WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.NAME, "name")))

        # проверяем, что логин в ЛК совпадает с первоначальным при авторизации
        Element = driver.find_element(By.NAME, "name")
        assert Element.get_attribute('value') == Email

        driver.quit()

    # проверяем авторизацию через кнопку в форме восстановления пароля
    def test_auth_button_from_password_recovery_form(self):
        # открыли страницу
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

        # сначала регистрируем нового пользователя

        # нажали на кнопку "Войти"
        driver.find_element(By.XPATH, ".//section[2]/div/button").click()
        # ожидание страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться")))
        # нажали на кнопку "Зарегистрироваться"
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
        # ожидание страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))

        # ввели имя
        driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("Alina")
        # ввели логин (почта)
        Email = f"alina_loginova_1_{random.randint(100, 999)}@gmail.com"
        driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(Email)
        # ввели пароль
        driver.find_element(By.NAME, "Пароль").send_keys("QWASZX12")
        # нажали кнопку "Зарегистрироваться"
        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()


        # теперь авторизуемся под учеткой созданного пользователя

        # открываем страницу авторизации
        driver.get("https://stellarburgers.nomoreparties.site/login")

        # нажимаем кнопку "Восстановить пароль"
        driver.find_element(By.XPATH, ".//*[@id='root']/div/main/div/div/p[2]/a").click()
        # ожидание страницы
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))

        # на открывшейся форме нажимаем кнопку "Войти"
        driver.find_element(By.LINK_TEXT, "Войти").click()

        # ожидание страницы авторизации
        WebDriverWait(driver, 2000).until(
            expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text()='Войти']")))
        # ввели логин (почта)
        driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys(Email)
        # ввели пароль
        driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys("QWASZX12")
        # нажали кнопку "Войти"
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

        # ожидание страницы после авторизации
        WebDriverWait(driver, 2000).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Личный Кабинет")))
        # переходим в ЛК по кнопке "Личный кабинет"
        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        # ожидание страницы ЛК
        WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.NAME, "name")))

        # проверяем, что логин в ЛК совпадает с первоначальным при авторизации
        Element = driver.find_element(By.NAME, "name")
        assert Element.get_attribute('value') == Email

        driver.quit()


