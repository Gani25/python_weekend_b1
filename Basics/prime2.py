# WAP to print series of prime number from 1 to n
# n = 100
# 2 3 5 7 11 ....

n = int(input("Enter a number: "))

i = 2
if(n >= 2):
    print(f"Series of prime number from 1 to {n}: ")
else:
    print(f"Enter positive number greater than 1 to get results")
while(i <= n):
    j = 2
    # Any Value of i is a prime number
    is_prime = True

    while (j <= i/2):
        remainder = i % j 
        if remainder == 0:
            is_prime = False
            break
        j += 1
    
    if is_prime:
        print(f"{i} ", end="")

    i += 1