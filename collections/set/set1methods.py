# Set -> It will store unique occurrence of Data

my_set = set()

print(my_set)
print(type(my_set))

my_set.add(50)
my_set.add(10)
my_set.add(100)
my_set.add("SPRK")
my_set.add(10)
my_set.add(5)
my_set.add(25)
my_set.add(50)
my_set.add("Hello")

print(my_set)
my_set.discard("Hello")
print(my_set)
my_set.discard(2055)
print(my_set)

# my_set.remove(2055)
# print(my_set)


print(my_set.pop())

print(my_set)
