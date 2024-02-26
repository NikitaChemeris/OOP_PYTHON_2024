class Cat():
    __shared_attr = {
        'breed': 'pers',
        'color': 'black'
    }
    
    def __init__(self):
         self.__dict__ = Cat.__shared_attr


"""
Example

d = Cat()
g = Cat()
d.breed = 'seam'        #it would be in g also
d.name = 'Bob'          #the same

"""