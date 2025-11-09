import datetime as dt
class football_player:

    def __init__(self, first_name, last_name, birth_year, gender, team):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.birth_year = birth_year
        self.team = team 
        self.goals = []# Empty run score array

    
    def add_goals(self, *player_goals):
        self.goals.extend(player_goals)

    def total_goals(self):
        return sum(self.goals)
    
    def average_goals(self):
        return sum(self.goals) / len(self.goals)

    def calculate_age(self):
        return dt.datetime.now().year - self.birth_year

    def __str__(self):
        
        return f"----------------------------------------------------------------\nFootball Player Information\nFirst Name = {self.first_name}\nLast Name = {self.last_name}\nGender = {self.gender}\nBirth Year = {self.birth_year}\nAge = {self.calculate_age()}\nGoals = {self.goals}\nTotal Goals = {self.total_goals()}\nAverage Goals = {self.average_goals()}\n----------------------------------------------------------------"
        