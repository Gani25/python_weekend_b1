class person_info:

    def __init__(self, first_name, last_name, gender, age):
        print("Person object is created")
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age=age

shubham = person_info("Shubham","Mhatre","Male",30)
print("Person Info")
print(f"First Name = {shubham.first_name}")
print(f"Last Name = {shubham.last_name}")
print(f"Gender = {shubham.gender}")
print(f"Age = {shubham.age}")
pranjali = person_info(first_name="Pranjali", age=20, last_name="Shinde", gender="Female")

print("Person Info")
print(f"First Name = {pranjali.first_name}")
print(f"Last Name = {pranjali.last_name}")
print(f"Gender = {pranjali.gender}")
print(f"Age = {pranjali.age}")
  