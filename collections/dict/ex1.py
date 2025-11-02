# WAP to create a dictionary

rohan = {
    "roll_no":101,
    "name":"Rohan Yadav",
    "marks":[50,60,80,90,50]
}

print(rohan)

print(rohan["name"])
rohan["gender"] = "Male"

print(rohan)

# Update
rohan["gender"] = "Other"
print(rohan)

rohan.pop("gender")
print(rohan)

rohan.update({"Gender":"Male","Phone":"123456789"})
print(rohan)

print(rohan.get("name"))
print(rohan.get("Name","Not Found"))

for key in rohan.keys():
    print(f"{key} : {rohan.get(key)}")

print( rohan.items())

for key,value in rohan.items():
    print(f"{key} = {value}")

rohan["average"] = sum(rohan["marks"]) / len(rohan["marks"])

print(rohan)