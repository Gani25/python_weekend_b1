# WAP to print series of prime number from 1 to n

def is_prime(number):
    i = 2

    while(i <= number // 2):
        if(number % i == 0):
            # Not Prime -> STOP
            return False

        i += 1
    return True

num = int(input("Enter a number to print series of prime number: "))

# Loop - 2 --- num

if(num > 1):
    print(F"Series of prime number from 1 to {num}")
else:
    print("Number should be greater than 1 to print series of prime number")
for i in range(2,num+1):

    if(is_prime(i)):
        print(f"{i} ",end="")

