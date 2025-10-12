# WAP to print first n natural numbers
# 1 2 3 4 ..... n

num = int(input("Enter a number to display natural numbers: "))

i = 1

if(num < 1):
    print("Natural number should be positive and greater than 0")
    
else:
    print(f"First {num} natural numbers are: ")
    while(i <= num):
        print(i)

        i = i + 1

# 4. WAP to print first n natural numbers in reverse order