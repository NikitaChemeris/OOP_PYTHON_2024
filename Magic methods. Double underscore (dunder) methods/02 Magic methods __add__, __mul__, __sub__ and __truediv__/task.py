class Vektor:
    
    def __init__(self, *args):
        self.values = sorted([i for i in args if isinstance(i, int)])

    def __str__(self):
        if self.values:
            inversion_str = [str(i) for i in self.values]
            return f"Vektor({', '.join(inversion_str)})"
        else:
            return "Empty Vektor"
    
    def __add__(self, other):
        new_values = []
        if isinstance(other, Vektor):
            if len(self.values) == len(other.values):
                for i in range(len(self.values)):
                    new_values.append(self.values[i] + other.values[i])
                return Vektor(*new_values)
            else:
                return "Addition of vectors of different lengths is not available"
        if isinstance(other, int):
            for i in range(len(self.values)):
                new_values = [i+other for i in self.values]
            return Vektor(*new_values)
        else:
            print(f"Vector cannot be added to <{other}>")
        
    def __mul__(self, other):
        new_values = []
        if isinstance(other, Vektor):
            if len(self.values) == len(other.values):
                for i in range(len(self.values)):
                    new_values.append(self.values[i] * other.values[i])
                return Vektor(*new_values)
            else:
                return "Multiplication of vectors of different lengths is not available"
        if isinstance(other, int):
            for i in range(len(self.values)):
                new_values = [i*other for i in self.values]
            return Vektor(*new_values)
        else:
            print(f"Vector cannot be multiplied to <{other}>")

"""
Example

v1 = Vektor(2, 1, 3)
print(v1)
v2 = Vektor(2, 3, 4)
print(v2)
v3 = v1 + v2
print(v3)
v4 = v3 + 5
print(v4)
v5 = v1 * 2
print(v5)
v5 * 'hi'
"""   