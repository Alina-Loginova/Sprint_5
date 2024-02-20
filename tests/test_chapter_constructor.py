from selenium import webdriver
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestConstructor:

    # проверяем переход к разделу "Булки"
    def test_constructor_go_to_buns(self):
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

        # ожидание загрузки страницы конструктора
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")))

        # выбрать булку
        driver.find_element(By.XPATH, ".//section[1]/div[2]/ul[1]/a[1]").click()

        # ожидание загрузки "Детали ингредиента"
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")))

        Page_Buns = driver.find_element(By.XPATH, ".//section[1]/div[2]")
        assert 'Флюоресцентная булка R2-D3' in Page_Buns.text

    # проверяем переход к разделу "Соусы"
    def test_constructor_go_to_sauces(self):
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

        # ожидание загрузки страницы конструктора
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")))

        # выбрать раздел "Соусы"
        driver.find_element(By.XPATH, ".//section[1]/div[1]/div[2]/span").click()

        # выбрать соус
        driver.find_element(By.XPATH, ".//section[1]/div[2]/ul[2]/a[1]").click()

        Page_Sauces = driver.find_element(By.XPATH, ".//*[@id='root']/div/section[1]/div[1]/div")
        assert 'Соус Spicy-X' in Page_Sauces.text

    # проверяем переход к разделу "Начинки"
    def test_constructor_go_to_fillings(self):
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
        Email = f"alinaloginova_1_{random.randint(100, 999)}@gmail.com"
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

        # ожидание загрузки страницы конструктора
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")))

        # выбрать раздел "Начинки"
        driver.find_element(By.XPATH, ".//section[1]/div[1]/div[3]/span").click()

        # выбрать начинку
        driver.find_element(By.XPATH, ".//section[1]/div[2]/ul[3]/a[1]").click()

        Page_Fillings = driver.find_element(By.XPATH, ".//*[@id='root']/div/section[1]/div[1]/div/p")
        assert 'Мясо бессмертных моллюсков Protostomia' in Page_Fillings.text
