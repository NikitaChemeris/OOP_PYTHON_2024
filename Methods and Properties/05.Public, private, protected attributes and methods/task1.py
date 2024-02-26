class Student():
    def __init__(self, name, age, branch):
        self.__name = name
        self.__age = age
        self.__bramch = branch
    
    def __display_details(self):                #it can work only in class
        print(f'Name: {self.__name}', f'Age: {self.__age}', f'Branch: {self.__bramch}', sep='\n')
    
    def access_private_method(self):
        self.__display_details()            


"""
Example

obj = Student("Adam Smith", 25, "Information Technology")
obj.access_private_method()

"""