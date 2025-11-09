import player_module as pm

# Derived Class -> Sub Class
class cricket_player(pm.player):

    def __init__(self, first_name, last_name, birth_year, gender, team):
        super().__init__(first_name, last_name, birth_year, gender, team)
        self.runs = []

    def add_runs(self, *player_runs):
        self.runs.extend(player_runs)

    def total_scores(self):
        return sum(self.runs)
    
    def average_scores(self):
        return sum(self.runs) / len(self.runs)
    
    def __str__(self):
        return super().__str__() + f"----------------------------------------------------------------\nCricket Player Information\nRuns = {self.runs}\nTotal Runs = {self.total_scores()}\nAverage Runs = {self.average_scores()}\n----------------------------------------------------------------\n"
    

# // Try same for FootBall Player