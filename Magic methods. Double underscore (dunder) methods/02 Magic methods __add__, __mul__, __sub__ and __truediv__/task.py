class Vektor:
    
    def __init__(self, *args):
        for symvol in args:
            if not isinstance(symvol, int):
                args.remove(symvol)
        
        self.values = sorted(args)
    
    def __str__(self):
        if len(self.values) > 0:
            return f"Vektor{tuple(self.values)}"
        else:
            return "Empty Vektor"
    
    def __add__(self, other):
        if isinstance(other, Vektor):
            if len(self.values) == len(other.values):
                self.new_values = []
                for i in range(len(self.values)):
                    self.new_values.append(self.values[i] + other.values[i])
                return f"Vektor{tuple(self.new_values)}"
            else:
                return "Multiplication of vectors of different lengths is not available"
        if isinstance(other, int):
            for i in range(len(self.values)):
                self.values[i] += other
            return f"Vektor{tuple(self.values)}"
        else:
            return "Vector cannot be added to <value>"