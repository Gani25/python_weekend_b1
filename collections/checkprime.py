# WAP to check whether the number is prime number or not
# also display all the list of factors

def check_prime():
    n = int(input("Enter a number: "))

    is_prime = None
    if(n <= 1):
        is_prime = False
        print("Enter positive number greater than one")
        return
    
    count = 0
    factors = []
    for i  in range(1,n+1):

        if(n % i == 0):
            count = count + 1
            factors.append(i)

    
    if count == 2:
        print(f"Number = {n} is a prime number")
        print(f"Its only factors are {factors[0]} and {factors[1]} ")
    else:    
        print(f"Number = {n} is NOT a prime number")
        print(f"All factors of {n}:")
        for index in range(0,len(factors)):
            if(index < len(factors)-1):
                print(factors[index], end=", ")
            else:
                print(factors[index], end=" ")

        # for factor in factors:
        #     print(factor, end=" ")


check_prime()