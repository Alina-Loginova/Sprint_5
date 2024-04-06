from selenium.webdriver.common.by import By

class Locators:

    # формы
    REGISTRATION_FORM = By.CLASS_NAME, "Auth_login__3hAey"  # форма регистрации
    COLLECT_BURGER = By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2"  # форма "Соберите бургер" в Конструкторе

    # кнопки
    REGISTRATION_BUTTON = By.XPATH, ".//button[text()='Зарегистрироваться']"  # кнопка "Зарегистрироваться"
    LOGIN_BUTTON = By.XPATH, ".//button[text()='Войти']"  # кнопка "Войти"
    LOGIN_IN_ACCOUNT_BUTTON = By.XPATH, ".//button[text()='Войти в аккаунт']"  # кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON_FOR_OLD_PERSON = By.LINK_TEXT, "Войти"  # кнопка "Войти" для ранее зарегистрировванных пользователей
    LOGIN_BUTTON_IN_RESTORE_PASSWORD = By.CLASS_NAME, "Auth_link__1fOlj"  # кнопка "Войти" на странице восстановления пароля
    RESTORE_PASSWORD_BUTTON = By.LINK_TEXT, "Восстановить пароль"  # кнопка "Восстановить пароль" на странице регистрации
    PERSONAL_ACCOUNT_BUTTON = By.LINK_TEXT, "Личный Кабинет"  # кнопка "Личный кабинет" на главной странице
    CONSTRUCTOR_BUTTON = By.LINK_TEXT, "Конструктор"  # кнопка "Конструктор"
    LOGO_BUTTON = By.CLASS_NAME, "AppHeader_header__logo__2D0X2"  # кнопка логотипа Stellar Burgers
    LOGOUT_BUTTON = By.XPATH, ".//button[text()='Выход']"  # кнопка "Выход"

    # поля Имя, Email, Пароль
    REGISTRATION_NAME_FIELD = By.XPATH, ".//label[text()='Имя']/following-sibling::input"  # поле "Имя" в регистрации
    REGISTRATION_EMAIL_FIELD = By.XPATH, ".//label[text()='Email']/following-sibling::input"  # поле "Email" в регистрации
    REGISTRATION_PASSWORD_FIELD = By.NAME, "Пароль"  # поле "Пароль" в регистрации
    AUTH_EMAIL_FIELD = By.XPATH, ".//*[text()='Email']/following-sibling::input"  # поле "Email" в авторизации
    AUTH_PASSWORD_FIELD = By.XPATH, ".//input[@type = 'password']"  # поле "Пароль" в авторизации
    PERSONAL_ACCOUNT_FIELD_LOGIN = By.NAME, "name"  # поле логина в Личном кабинете

    # разделы в Конструкторе
    PAGE_BUNS = By.XPATH, ".//span[text()='Булки']/parent::div"  # раздел "Булки" в Конструкторе
    PAGE_SAUCES = By.XPATH, ".//span[text()='Соусы']/parent::div"  # раздел "Соусы" в Конструкторе
    PAGE_FILLINGS = By.XPATH, ".//span[text()='Начинки']/parent::div"  # раздел "Начинки" в Конструкторе

    # ошибки
    TEXT_ABOUT_ERROR = By.CLASS_NAME, "input__error"  # сообщение об ошибке "Некорректный пароль"
