student_info = {
    "rohan":{
        "roll_no":101,
        "name":"Rohan Rajput",
        "gender":"Male",
        "marks":[50,60,90,80,55]
    },
    "shiva":{
        "rollno":102,
        "name":"Shiva Sharma",
        "gender":"Male",
        "marks":[98,66,99,88,58]
    }
}
print(student_info)

for key, value in student_info.items():
    print("----------------------------------------------------")
    print(f"{key.upper()} Information")
    print(value)