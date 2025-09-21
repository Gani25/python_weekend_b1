# WAP to check whether the number is divisible by 2 or not
# Divisible by 2 -> Divide the number by 2 and 
    #  check remainder (%)
    # if remainder is 0 -> Number is divisible by 2
    # if remainder is not 0 -> Number is not divisible by 2
# Input = 1, conditions = 2 (if else)

num = int(input("Enter a number: "))

remainder = num % 2
if remainder == 0:
    print(f"Number = {num} is divisible by 2")
    print(f"Number = {num} is even")

else:
    print(f"Number = {num} is not divisible by 2")
    print(f"Number = {num} is odd")

'''
3. WAP to check whether the number is zero or non zero
if num == 0:
    print("Number is Zero")
else:
    print("Number is Non Zero")

4. WAP to check whether the number is divisible by 5 or not
if num % 5 == 0:
    print("Number is divisible by 5")
else
    print("Number is not divisible by 5")
5. WAP to check whether the number is less than 18 or not
    if less than 18 display 
    your age = {age} is below 18 you are not eligible for license
    if greater than or equal to 18 then display 
    your age = {age} is above or equal to 18 you are eligible for license

    age = int(input("Enter your age"))
'''
