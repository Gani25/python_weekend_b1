# WAP to check whether the last digit of number is divisible by 3 or not
# ex num = 159 -> last_digit = 9 -> divisible by 3

num = int(input("Enter a number: "))
last_digit = num % 10

if last_digit % 3 == 0:
    print(f"Number = {num}, Last digit = {last_digit} is divisible by 3")
else:
    print(f"Number = {num}, Last digit = {last_digit} is not divisible by 3")
    
    
    