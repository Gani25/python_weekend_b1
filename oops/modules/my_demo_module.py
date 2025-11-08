def addition(n1:int, n2: int  = 0, *numbers:int):
    return n1+n2+sum(numbers)


def products(n1:int, n2: int  = 0, *numbers:int):
    result = 1
    for num in numbers:
        result = result * num
    return n1*n2 * result

def check_prime(num:int):
    if num <= 1:
        return False
    for i in range(2,num):

        if num % i == 0:
            # not prime -> exit

            return False
    return True

def check_prime_display(num:int):
    if check_prime(num):
        return f"Number = {num} is a prime number"
    
    return  f"Number = {num} is not a prime number"
