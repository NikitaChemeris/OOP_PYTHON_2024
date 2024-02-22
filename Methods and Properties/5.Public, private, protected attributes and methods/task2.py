class PizzaMaker():
    def __make_pepperoni(self):
        pass
    
    def _make_barbecue(self):
        pass

"""
Example

print(PizzaMaker.__dict__.keys())       #for watching free atributes
maker = PizzaMaker()
maker._make_barbecue()                  #_ - it's warning for programmator from other programmator, that it's better using only in class
maker._PizzaMaker__make_pepperoni()     #for watching private atributes
"""