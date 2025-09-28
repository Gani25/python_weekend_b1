# WAP to print factorial of 5
# 5 * 4 * 3 * 2 * 1 = 120
# start = 5, stop = 1, gap = -1


i = 5
fact = 1

while(i >= 1):

    fact = fact * i 

    i = i - 1

print(f"The Factorial of 5 is {fact}")