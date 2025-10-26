# Nested List -> 2D Arrays/ Matrix

students = [
    ["Roll No","Name","Marks"],
    [1,"Anjali",65],
    [2,"Shivanand",99],
    [3,"Saurabh",50],
    [4  ,"Rakesh",10],
]

print(students[0])
print(students[0][2])
print(students)

print("Slicing")
print(students[1:])
print(students[::-1])
print(students[:][0])

# Looping over List
print("Looping Over Array")
for row in students:
    print(row)
print("Display Name and Marks")
for row in students:
    print(row[1:])
print("Looping Over Array and displaying individual element")
for row in students:
    for element in row:
        print(element)