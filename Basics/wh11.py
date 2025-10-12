# WAP to print sum of digit of n
# n = 153 -> 3 + 5 + 1 = 9

n = int(input("Enter a number: "))

sum = 0
i = n 

while(i != 0):
    last_digit = i % 10
    sum = sum + last_digit

    i = i // 10

print(f"The sum of digit of {n} = {sum}")