1. Описание:

Что тестируем: сервис Stellar Burgers (https://stellarburgers.nomoreparties.site/)
Для тестирования используем Google Chrome

2. Запуск тестов:

Запустить тесты можно с помощью команды: pytest *название необходимого файла*
Пример: pytest test_registration.py


3. Описание тестов из папки test:

# Общая папка, в которой хранятся все тесты
tests
# тестируем регистрацию нового клиента
    test_registration
        test_registration_correct # проверяем, что регистрация прошла успешно
        test_registration_incorrect_password_two_symbols # проверяем ошибку при регистрации с паролем менее 6 символов
# тестируем авторизацию ранее зарегистрированного клиента
    test_authorization 
        class TestAuthorization # класс, в котором хранятся тесты
            test_auth_button_from_home # проверяем авторизацию через кнопку "Войти в аккуант"
            test_auth_button_from_personal_account # проверяем авторизацию через кнопку «Личный кабинет»
            test_auth_button_from_register # проверяем авторизацию через кнопку в форме регистрации
            test_auth_button_from_password_recovery_form # проверяем авторизацию через кнопку в форме восстановления пароля
# тестируем переход в Личный кабинет
    test_go_to_personal_account
        test_go_to_personal_account # проверяем переход в Личный кабинет
# тестируем переход из Личного кабинета в Конструктор
    test_from_personal_account_to_constructor
        test_from_personal_account_to_constructor # по кнопке "Конструктор"
        test_from_personal_account_to_logo # по кнопке логотипа "Stellar Burgers"
# тестируем раздел Конструктора
    test_chapter_constructor    
        test_constructor_go_to_buns # проверяем переход к разделу "Булки"
        test_constructor_go_to_sauces # проверяем переход к разделу "Соусы"
        test_constructor_go_to_fillings # проверяем переход к разделу "Начинки"
# тестируем выход из учетной записи
    test_logout
        test_logout_correct # проверяем, что клиент успешно выходит из своей учетной записи



