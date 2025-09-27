# 1. Accept a number and check whether the number have 3 digit or not

num= int(input("Enter a number : "))


if (num>=100 and num<=999) or (num <= -100 and num >= -999):
    print(f"The {num} contains three(3) digit")
else:
    print(f"The {num} doesn't contains three(3) digit")