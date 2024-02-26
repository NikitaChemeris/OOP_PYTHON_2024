class Point():
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, other_point):
        if (hasattr(self, 'x') and hasattr(self, 'y'))  and (hasattr(other_point, 'x') and hasattr(other_point, 'y')):
            print(f'{((other_point.x - self.x)**2 + (other_point.y - self.y)**2)**0.5}')
        else:
            print("Not a valid point")

p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
d = p1.get_distance(p2)
p1.get_distance(10)