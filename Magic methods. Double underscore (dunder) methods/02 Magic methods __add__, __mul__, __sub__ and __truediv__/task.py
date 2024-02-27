class Vektor:

    def __init__(self, *args):
        for symvol in args:
            if not isinstance(symvol, int):
                args.remove(symvol)
        
        self.values = sorted(args)

    def __str__(self):
        if len(self.values) > 0:
            return self.values
        