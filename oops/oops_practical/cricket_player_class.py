import datetime as dt
class cricket_player:

    def __init__(self, first_name, last_name, birth_year, gender, team):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.birth_year = birth_year
        self.team = team 
        self.runs = []# Empty run score array

    
    def add_runs(self, *player_runs):
        self.runs.extend(player_runs)

    def total_scores(self):
        return sum(self.runs)
    
    def average_scores(self):
        return sum(self.runs) / len(self.runs)

    def calculate_age(self):
        return dt.datetime.now().year - self.birth_year

    def __str__(self):
        
        return f"----------------------------------------------------------------\nCricket Player Information\nFirst Name = {self.first_name}\nLast Name = {self.last_name}\nGender = {self.gender}\nBirth Year = {self.birth_year}\nAge = {self.calculate_age()}\nRuns = {self.runs}\nTotal Runs = {self.total_scores()}\nAverage Runs = {self.average_scores()}\n----------------------------------------------------------------"
        