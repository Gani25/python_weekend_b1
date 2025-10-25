# WAF to calculate sum of whole number from 0 to n using recurrsion
def calSum(number):
    if(number < 0):
        return -1
    if(number == 0):
        return 0
    if(number == 1):
        return 1
    return number + calSum(number-1)

num = int(input("Enter a number: "))

ans = calSum(num)
if(ans == 0):
    print(f"Sum of {num} = {ans}")
elif ans == -1:
    print(f"Enter positive number only")
else:
    print(f"Sum of 1 to {num} = {ans}")