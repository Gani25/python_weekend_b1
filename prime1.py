# WAP to print series of prime number from 1 to n
# n = 100
# 2 3 5 7 11 ....

# Check whether the number is a prime number or not
n = int(input("Enter a number: "))
is_prime = True
if(n <= 1):
    is_prime = False
i = 2
while(i <= n/2):
    remainder = n % i 
    if remainder == 0:
        is_prime = False
        break
    i += 1

if is_prime:
    print(f"Number: ${n} is a prime number")
else:
    print(f"Number: ${n} is not a prime number")