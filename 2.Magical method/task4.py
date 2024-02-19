class SoccerPlayer():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0
    
    def score(self, score=1):
        self.score = score
        self.goals += self.score
    
    def make_assists(self, make_assists=1):
        self.make_assists = make_assists
        self.assists += self.make_assists
    
    def statisticks(self):
        print("{} {} - goals: {}, assists: {}".format(self.surname, self.name, self.goals, self.assists))

