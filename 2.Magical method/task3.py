class Laptop():
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = brand + " " +  model

hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.price)
print(hp.laptop_name)

laptop1 = Laptop('apple', 'macbook-13pro', 120000)
laptop2 = Laptop('lenovo', 'goholin-22h', 21000)
