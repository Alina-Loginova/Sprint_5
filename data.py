class User:

    def __init__(self, name):
        self.__name = name
        self.__email = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value


