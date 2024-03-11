class Quadrilateral:

    def __init__(self, width, height = None):
        if height is None:
            self.width = self.height = width
        else:
            self.width = width
            self.height = height

    def __str__(self):
        if self.width == self.height:
            return f"Cube size {self.width}x{self.height}"
        else:
            return f"Rectangle size {self.width}x{self.height}"
        
    def __bool__(self):
        return self.width == self.height

"""
Example

q1 = Quadrilateral(10)
print(q1)
print(bool(q1))
q2 = Quadrilateral(3, 5)
print(q2)
print(q2 == True)
"""