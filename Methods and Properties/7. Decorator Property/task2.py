class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars*100+cents

    @property
    def dollars(self):
        return self.total_cents // 100
    
    @property
    def cents(self):
        return self.total_cents % 100
    
    @dollars.setter
    def dollars(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError('Error dolars')
        self.total_cents = value*100 + self.cents
    
    @cents.setter
    def cents(self, value):
        if not isinstance(value, int) or 0 <= value > 99:
            raise ValueError('Error cents')
        self.total_cents = self.dollars*100 + value

    def __str__(self):
        return f'Your balance is {self.total_cents // 100} dollars and {self.total_cents % 100} cents'

"""
Example

Bill = Money(101, 99)
print(Bill)
print(Bill.dollars, Bill.cents)
print(Bill.total_cents)
Bill.dollars = 666
print(Bill)
Bill.cents = 12
print(Bill)
"""