import string

class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password
    
    @staticmethod                       #checking number in values
    def is_include_digit(password):
        for symvol in password:
            if symvol in string.digits:
                return True
        else:
            return False
    
    @staticmethod
    def is_include_all_register(password):
        repeat_actions = 0
        for symvol in password:
            if symvol in string.ascii_uppercase:
                repeat_actions += 1
        if repeat_actions > 1:
            return True
        else:
            return False
    
    @staticmethod
    def is_include_only_latin(password):
        for symvol in password:
            if symvol not in string.ascii_letters and symvol not in string.digits and symvol not in string.punctuation:
                return False
        else:
            return True
    
    @staticmethod
    def check_password_dictionary(password):
        with open('Methods and Properties\\10. Practice property\\easy_passwords.txt', 'r') as f:
            common_passwords = f.readlines()
            for unsafe_pass in common_passwords:
                if password == unsafe_pass.strip():
                    return False
            else:
                return True
    
    @property
    def login(self):
        return self.__login
    
    @property
    def password(self):
        print('getter called')
        return self.__password
    
    @login.setter
    def login(self, value):
        print('setter login called')
        if '@' not in value:
            raise ValueError("Login must include at least one '@'")
        if '.' not in value:
            raise ValueError("Login must include at least one '.'")
        self.__login = value
    
    @password.setter
    def password(self, value):
        print('setter password called')
        if not isinstance(value, str):
            raise TypeError("Password must be string")
        if 4 > len(value) or len(value) > 12:
            raise ValueError("Password must be longer than 4 and shorter than 12 symbols")
        if not Registration.is_include_digit(value):
            raise ValueError("The password must have at least one digit")
        if not Registration.is_include_all_register(value):
            raise ValueError("The password must contain at least two capital letters")
        if not Registration.is_include_only_latin(value):
            raise ValueError("The password must contain only the Latin alphabet")
        if not Registration.check_password_dictionary(value):
            raise ValueError('Your password is on the list of the easiest passwords.')
        self.__password = value

"""
Example

user = Registration('enjind@yuo.oi', 'QWertyuop1')
print(user.login)
print(user.password)
"""