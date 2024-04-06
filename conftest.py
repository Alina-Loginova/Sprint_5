import random
import pytest
from selenium import webdriver
from data import User


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()

@pytest.fixture
def user():
    user = User(name='Alina')
    user.email = f'alina_loginova_1_{random.randint(100, 9999)}@gmail.com'
    return user
