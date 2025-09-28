# WAP to check whether the number is prime number or not
# Prime number -> Divisible by 1 and by itself
# start = 2, stop = n-1, gap = 1

n = int(input("Enter a number: "))

# Assuming any value of n is a prime number
is_prime = True

# if n is -ve or = 1 then it is not a prime number
if(n <= 1):
    is_prime = False
i = 2 

while(i <= n-1):
    if n % i == 0:
        # number is not a prime number
        is_prime = False
        break
    
    i = i + 1

if is_prime == True:
    print(f"Number = {n} is a prime number")
else:
    print(f"Number = {n} is not a prime number")

'''
1. WAP to display fizz buzz iterate from 1 to n
Based on criteria display message
a. if num is divisible by 3 and 5 both -> FIZZBUZZ
b. if num is divisible by 3 -> FIZZ
c. if num is divisible 5 -> BUZZ
d. if num is not divisible by 3 and 5 -> display number

'''