import datetime as dt
virat={
    "First_name":"Virat",
    "Last_name":"Kohli",
    "gender":"Male",
    "team":"India",
    "birthyear":1970,
    "score":[],
}

# score add
def addScores(list_scores, *cricket_scores):
    list_scores.extend(cricket_scores)

def calculate_age(player_birth_year):
    return dt.datetime.now().year - player_birth_year

def calculate_sum(list_scores):
    return None 
def calculate_average(list_scores):
    return None 
virat_score = virat["score"]
addScores(virat_score,50,60,80)
print(virat_score)
print(virat)
addScores(virat_score,20,60)
print(virat)


print("Player Info")
print(f"Name = {virat['First_name']} {virat["Last_name"]}")
print(F"Gender = {virat['gender']}")
print(F"Team = {virat['team']}")
print(F"Birth Year = {virat['birthyear']}")
print(F"Age = {calculate_age(virat['birthyear'])}")
print(F"Runs = {virat['score']}")
print(F"Total Runs = {virat['score']}")
print(F"Total Average = {virat['score']}")
sachin = {
    "First_name":"sachin",
    "Last_name":"Tendulkar",
    "gender":"Male",
    "team":"India",
    "birthyear":1945,
    "score":[],
}