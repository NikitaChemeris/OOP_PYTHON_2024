class City:
    
    def __init__(self, name_city):
        self.name = name_city.lower().title()
        
    def __str__(self):
        return self.name

    def __bool__(self):
        return True if self.name[-1] not in ("a", "e", "i", "o", "u") else False
    
"""
Example

p1 = City('new york')
print(p1)
print(bool(p1))
p2 = City('SaN frANCISco')
print(p2)
print(p2 == True)
"""