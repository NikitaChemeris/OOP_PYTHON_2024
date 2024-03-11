from functools import total_ordering

@total_ordering
class ChessPlayer:

    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, int):
            return self.rating == other
        elif isinstance(other, ChessPlayer):
            return self.rating == other.rating
        else:
            return "Unable to perform a comparison"
        
    def __lt__(self, other):
        if isinstance(other, int):
            return self.rating < other
        elif isinstance(other, ChessPlayer):
            return self.rating < other.rating
        else:
            return "Unable to perform a comparison"
    

"""
Example 

magnus = ChessPlayer ('Carlsen', 'Magnus', 2847)
ian = ChessPlayer ('Ian', 'Nepomniachtchi', 2789)
print(magnus == 4000)
print(ian == 2789)
print(magnus == ian)
print(magnus > ian)
print(magnus < ian)
print (magnus < [1, 2])
"""