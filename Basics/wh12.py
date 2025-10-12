# WAP to check whether the number is palindrome or not
# ex = n = 1551 -> rev = 1551 n == rev -> Palindrome
# ex = n = 153 -> rev = 351 n != rev -> Not Palindrome

n = int(input("Enter a number: "))
i = n 

rev = 0

while(i != 0):
    last_digit = i % 10

    rev = rev * 10 + last_digit

    i = i // 10

if n == rev:
    print(f"Number = {n} is a palindrome number")
else:
    print(f"Number = {n} is not a palindrome number, Reverse = {rev}")

# WAP to check whether the number is perfect number or not
'''
Example:
n = 28
sum of all divisor except number is equal to n -> Perfect Number
1 + 2 + 4 + 7 + 14 = 28
n = 6
1 + 2 + 3 = 6
'''