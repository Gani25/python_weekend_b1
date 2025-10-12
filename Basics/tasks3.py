# 3. Count Even and Odd Digits in a Number
# Example -> Input: 24613 → Output: Even=3, Odd=2

n = int(input("Enter a number: "))

i = n 

evenCount = 0
oddCount = 0

while(i > 0):
    last_digit = i % 10
    if(last_digit % 2 == 0):
        evenCount += 1
    else:
        oddCount += 1
    
    i = i // 10


print(f"Number = {n}, Even Digits = {evenCount} and Odd Digits = {oddCount}")