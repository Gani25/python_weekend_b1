# Function accepting multiple values
# Excel -> sum(v1,v2,v3....)

# Function with args (*param)


def addition(*numbers):
    print(numbers)
    print(type(numbers))
    print(sum(numbers))

addition(5,6,10,12)