class person_info:

    def __init__(self, first_name, last_name, gender, age):
        print("Person object is created")
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age=age
    
    def check_eligible(self):
        if self.age <=18:
            return "Not Eligible For License"
        return "Eligible For License"
    
    def __str__(self):
        return f"Person Info\nFirst Name = {self.first_name}\nLast Name = {self.last_name}\nGender = {self.gender}\nAge = {self.age}\nEligibility = {self.check_eligible()}"

shubham = person_info("Shubham","Mhatre","Male",30)
print(shubham)
print(type(shubham))

pranjali = person_info(first_name="Pranjali", age=15, last_name="Shinde", gender="Female")
print(pranjali)
print(type(pranjali))

'''
Convert our dictonary of cricket player in cricket_player_module into class cricket_player
Write all the logic in that class

create another file named as -> cricket_player_main -> 2 objs
'''