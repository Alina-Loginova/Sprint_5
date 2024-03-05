import random
import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()

@pytest.fixture
def user():
    user.name = f'Alina'
    user.email = f'alina_loginova_1_{random.randint(100, 999)}@gmail.com'
    return user