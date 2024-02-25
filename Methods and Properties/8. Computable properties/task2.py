class Date:
    def __init__(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y

    @property
    def date(self):
        return '{:02d}/{:02d}/{:04d}'.format(self.day, self.month, self.year)
    
    @property
    def use_date(self):
        return '{:02d}-{:02d}-{:04d}'.format(self.month, self.day, self.year)


"""
Example

d1 = Date(5, 10, 2001)
d2 = Date(15, 3, 999)

print(d1.date)
print(d1.use_date)
print(d2.date)
print(d2.use_date)
"""
