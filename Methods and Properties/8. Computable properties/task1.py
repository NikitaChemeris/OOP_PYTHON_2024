class Rectangle:
    def __init__(self, h, w):
        self.height = h
        self.weight = w

    @property
    def area(self):
        return self.height * self.weight

"""
Example

r1 = Rectangle(3, 5)
r2 = Rectangle(6, 1)

print(r1.area)
print(r2.area)
"""
