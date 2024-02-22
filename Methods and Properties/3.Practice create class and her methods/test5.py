class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def discription(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, voice):
        self.voice = voice
        return f'{self.name} says {self.voice}'

"""
EXAMPLE

jack = Dog('Jack', 4)
print(jack.discription())
print(jack.speak('boooooooob'))
"""