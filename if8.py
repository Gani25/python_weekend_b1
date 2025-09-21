'''
WAP to accept 3 sides of triangle and check whether the triangle is
1. Check all sides are positive: if
    i. Equilateral : All sides are equal -> and if
    ii. Isoceles: Any 2 sides are equal -> or elif
    iii. Scalene: No sides are equal -> else 

2. ANy side is negative: else
    Invalid Triangle

'''
s1 = int(input("Enter side 1: "))
s2 = int(input("Enter side 2: "))
s3 = int(input("Enter side 3: "))
if s1 > 0 and s2 > 0 and s3 > 0:
    if s1 == s2 and s2 == s3:
        print("Equilateral triangle")

    elif s1 == s2 or s2 == s3 or s1 == s3:
        print("Iscocles triangle")

    else:
        print("Scalene triangle")
else:
    print("Invalid triangle")

# 1. Accept a number and check whether the number have 3 digit or not
# Do not use any function

# WAP to check whether the year is a leap year or not