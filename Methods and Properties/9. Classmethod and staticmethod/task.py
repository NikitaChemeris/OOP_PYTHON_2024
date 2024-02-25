class Robot:
    population = 0

    def __init__(self, n):
        self.name = n
        print(f"Robot {self.name} was created")
        Robot.population += 1

    def destroy(self):
        Robot.population -= 1
        print(f"Robot {self.name} was destroyed")

    def say_hello(self):
        print(f"Robot {self.name} is greeting you, human species")

    @classmethod
    def how_many(cls):
        print(f"{cls.population}, that's how many of us are left")


"""
Example

r2 = Robot("R2-D2")
r2.say_hello()
Robot.how_many()
r2.destroy()
"""