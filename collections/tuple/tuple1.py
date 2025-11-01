# Tuple -> are immutable -> Change Not Possible
# () / tuple()

my_numbers = ()

print(my_numbers)
print(type(my_numbers))


my_numbers = (5,1,7,9,3,5,6,3,9,5)

print(len(my_numbers))
print("Element at zero index: ",my_numbers[0])

# update element at 0 and set it to 1000
# my_numbers[0] = 1000
print("Element at zero index: ",my_numbers[0])

print(my_numbers.count(5))