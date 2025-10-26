list1 = [10,20,-6,30,50,90,100]

print("List 1:",list1)

list2 = list1
print("List 2:",list2)
list2.extend(["Hello",30,"SPRK"])
print("List 1:",list1)
print("List 2:",list2)

list3 = list1.copy()
print("List 1:",list1)
print("List 3:",list3)

list3.append("Bye")
print("List 1:",list1)
print("List 3:",list3)