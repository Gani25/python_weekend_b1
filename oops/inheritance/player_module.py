import datetime as dt

# BASE CLASS/ SUPER CLASS
class player:

    def __init__(self, first_name, last_name, birth_year, gender, team):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.birth_year = birth_year
        self.team = team 

    def calculate_age(self):
        return dt.datetime.now().year - self.birth_year

    def __str__(self):
        
        return f"----------------------------------------------------------------\nPlayer Information\nFirst Name = {self.first_name}\nLast Name = {self.last_name}\nGender = {self.gender}\nBirth Year = {self.birth_year}\nAge = {self.calculate_age()}\n----------------------------------------------------------------\n"
        