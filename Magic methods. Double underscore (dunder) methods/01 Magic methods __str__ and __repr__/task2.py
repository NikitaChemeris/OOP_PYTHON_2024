class Vector:

    def __init__(self, *args):
        self.values = args

    def __str__(self):
        if len(self.values) > 0:
            return f'Vector{tuple(sorted(self.values))}'
        else:
            return 'Empty vector'

"""
Example

v1 = Vector(1, 2, 3)
print(v1)
v2 = Vector()
print(v2)

"""