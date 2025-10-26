my_list = ["Banana","Banana","Orange","Litchi","Banana","Orange","Sweetlime","Banana"]

print(my_list)

print("Index of Banana =",my_list.index("Banana"))

print("Index of Banana start from 1 =",my_list.index("Banana",1))


print(my_list)
print("Index of Banana skip first 2 occurence Banana =",my_list.index("Banana",my_list.index("Banana",my_list.index("Banana")+1)+1))

my_list = ["Banana","Orange","Litchi","Banana","Orange","Sweetlime","Banana"]

print(my_list)
print("Index of Banana skip first 2 occurence Banana =",my_list.index("Banana",my_list.index("Banana",my_list.index("Banana")+1)+1))

my_list.remove("Banana")

print(my_list)

del my_list[1]
print(my_list)
print("Element deleted = ",my_list.pop())
print(my_list)

print("Element deleted at index 2 = ",my_list.pop(2))
print(my_list)

print(len(my_list))
my_list.append("Banana")
print(len(my_list))
my_list.append(["Kiwi","Orange","Banana","Mango","Banana","Litchi","GUava"])

print("Length of list = ",len(my_list))
print(my_list)
print("Element of list at index 4 = ",my_list[4])
print("Length of list at index 4 = ",len(my_list[4]))

print(my_list)
print("Number of time banana repeated: ",my_list.count("Banana"))
print(my_list)
print("Number of time banana repeated in both list: ",my_list.count("Banana")+my_list[4].count("Banana"))
