class Zebra():
    def __init__(self, number=0):
        self.number = number
    
    def which_stripe(self):
        self.number += 1
        if self.number % 2 != 0:
            print('line - white')
        else:
            print('line - black')