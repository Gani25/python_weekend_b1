'''
4. A perfect number is a positive integer that is equal to the sum of its proper positive divisors, excluding the number itself. Proper divisors are all positive divisors of a number, except for the number itself. 
For example: 
6 is a perfect number because its proper divisors are 1, 2, and 3. The sum of these divisors (1 + 2 + 3) is 6.
28 is a perfect number because its proper divisors are 1, 2, 4, 7, and 14. The sum of these divisors (1 + 2 + 4 + 7 + 14) is 28.
'''

n = int(input("Enter a number: "))

sum = 0
# FOR
for i in range(1,n):
    if(n % i == 0):
        sum = sum + i 
    

if(sum == n):
    print(f"Number = {n} is Perfect Number")
else:
    print(f"Number = {n} is Not a Perfect Number, Since sum of diviors = {sum}")