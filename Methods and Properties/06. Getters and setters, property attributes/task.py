class UserMail():
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        print(self.__email)
        
    def set_email(self, value):
        if value.count('@') == 1 == value.count('.'):
            self.__email = value
        else:
            raise ValueError(f'ErrorMail:{value}')
        
    email = property(fget=get_email,fset=set_email)
    
"""
Example

k = UserMail('belosnezhka', 'belosnezka@gmail,com')
print(k.email)
k.email = [1,2,3]
k.email = 'belosnezk@agmail@.com'
k.email = 'belosnezka2024@upset.ua'
print(k.email)

"""