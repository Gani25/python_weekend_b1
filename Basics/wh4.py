# 4. WAP to print first n natural numbers in reverse order

# start = n, stop = 1, gap = -1

num = int(input("Enter a number: "))

i = num 

print(f"First {num} natural numbers in reverse order are: ")
while (i >= 1):
    print(i)
    i = i - 1