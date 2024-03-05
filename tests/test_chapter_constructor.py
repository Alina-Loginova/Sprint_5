from locators import Locators

class TestConstructor:

    # проверяем переход к разделу "Булки"
    def test_constructor_go_to_buns(self, driver):

        # открыли стартовую страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

        # проверяем, что выбранный элемент относится к разделу "Булки"
        element = driver.find_element(*Locators.PAGE_BUNS)
        element_class = element.get_attribute('class')
        assert 'current' in element_class and 'Булки' in element.text

    # проверяем переход к разделу "Соусы"
    def test_constructor_go_to_sauces(self, driver):

        # открыли стартовую страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

        # переходим на раздел "Соусы"
        driver.find_element(*Locators.PAGE_SAUCES).click()

        # проверяем, что выбранный элемент относится к разделу "Соусы"
        element = driver.find_element(*Locators.PAGE_SAUCES)
        element_class = element.get_attribute('class')
        assert 'current' in element_class and 'Соусы' in element.text

    # проверяем переход к разделу "Начинки"
    def test_constructor_go_to_fillings(self, driver):

        # открыли стартовую страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

        # переходим на раздел "Начинки"
        driver.find_element(*Locators.PAGE_FILLINGS).click()

        # проверяем, что выбранный элемент относится к разделу "Начинки"
        element = driver.find_element(*Locators.PAGE_FILLINGS)
        element_class = element.get_attribute('class')
        assert 'current' in element_class and 'Начинки' in element.text
