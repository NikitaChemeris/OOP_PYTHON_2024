class Person:
    
    def __init__(self, name, surname, genger='male'):
        self.name = name
        self.surname = surname
        if genger != 'male' and genger != 'female':
            print("I don't know what you mean? Let it be a male!")
            self.genger = 'male'
        else:
            self.genger = genger
    
    def __str__(self):
        if self.genger == 'male':
            return f'Man {self.name} {self.surname}'
        else:
            return f'Woman {self.name} {self.surname}'

"""
Example

p1 = Person('Chuck', 'Norris')
print(p1)
p2 = Person('Mila', 'Kunis', 'female')
print(p2)
p3 = Person('Obi-Van', 'Kenobi', True)
print(p3)
"""