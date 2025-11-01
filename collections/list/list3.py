my_list = list()

print(my_list)

my_list.append("Apple")
my_list.append("Apple")
my_list.append("Apple")
my_list.append("Apple")
print(my_list)

my_list[1] = "Banana"
print(my_list) 

my_list[2] = "Litchi"
my_list[3] = "Watermellon"
print(my_list) 
my_list.insert(0,"Guava")
print(my_list) 
my_list.insert(2,"Peach")
print(my_list) 

my_list.append(["Orange","Mango","Pineapple"])
print(my_list) 


my_list.extend(["Orange","Mango","Pineapple"])
print(my_list) 