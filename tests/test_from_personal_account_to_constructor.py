from selenium import webdriver
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestFromPersonalAccountToConstructor:

    def test_from_personal_account_to_constructor(self):
        # открыли страницу
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

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

        # нажали на кнопку "Конструктор"
        driver.find_element(By.XPATH, ".//li[1]/a/p").click()
        # ожидание загрузки страницы
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")))

        # прокрутить до конца страницы с бургерами
        Page_Burgers = driver.find_element(By.XPATH, ".//section[1]/div[2]")
        driver.execute_script("arguments[0].scrollIntoView();", Page_Burgers)

        assert 'Сыр с астероидной плесенью' in Page_Burgers.text

    def test_from_personal_account_to_logo(self):
        # открыли страницу
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")

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

        # нажали на кнопку логотипа Stellar Burgers
        driver.find_element(By.CLASS_NAME, "AppHeader_header__logo__2D0X2").click()
        # ожидание загрузки страницы
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")))

        # прокрутить до конца страницы "Соберите бургер"
        Page_Burgers = driver.find_element(By.XPATH, ".//section[1]/div[2]")
        driver.execute_script("arguments[0].scrollIntoView();", Page_Burgers)

        assert 'Сыр с астероидной плесенью' in Page_Burgers.text

