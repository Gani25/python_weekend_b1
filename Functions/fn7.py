# Create a function which return bool based on number is prime or not

def is_prime(number):
    i = 2

    while(i <= number // 2):
        if(number % i == 0):
            # Not Prime -> STOP
            return False

        i += 1
    return True

num = int(input("Enter a number to check prime or not: "))

if(is_prime(num)):
    print(f"Number = {num} is a prime number")
else:
    print(f"Number = {num} is not a prime number")

# WAP to print series of prime number from 1 to n