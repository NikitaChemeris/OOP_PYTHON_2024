class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @staticmethod
    def is_include_digit():
        pass

    @property
    def login(self):
        return self.__login
    
    @property
    def password(self):
        return self.__password
    
    @property.setter
    def login(self, value):
        if '@' not in value:
            raise ValueError("Login must include at least one '@'")
        if '.' not in value:
            raise ValueError("Login must include at least one '.'")
        self.__login = value
    
    @property.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError('Password must be string')
        if 4 > len(value) or len(value) > 12:
            raise ValueError('Password must be longer than 4 and shorter than 12 symbols')


    