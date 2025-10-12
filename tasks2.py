'''
2. WAP to check whether the given number is Armstrong Number Or Not?
A positive integer of n digits is an Armstrong number of order n if the sum of each digit raised to the power of n equals the original number. 
Example:
Consider the number 153:
Count the number of digits: 153 has 3 digits, so n = 3.
Raise each digit to the power of n and sum them:
1^3 = 1
5^3 = 125
3^3 = 27
Sum = 1 + 125 + 27 = 153
Compare the sum with the original number: Since the sum (153) is equal to the original number (153), 153 is an Armstrong number.
Another Example:
Consider the number 1634:
Count the number of digits: 1634 has 4 digits, so n = 4.
Raise each digit to the power of n and sum them:
1^4 = 1
6^4 = 1296
3^4 = 81
4^4 = 256
Sum = 1 + 1296 + 81 + 256 = 1634
'''

n = int(input("Enter a number: "))

digit = 0

i = n 

while(i > 0):
    i = i // 10
    digit += 1

sum = 0
i = n 
while i > 0:
    last_digit = i % 10
    power = last_digit ** digit
    sum = sum + power

    i = i // 10

if n == sum:
    print(f"Number = {n} is Armstrong Number")
else:
    print(f"Number = {n}, sum = {sum} is not Armstrong Number")