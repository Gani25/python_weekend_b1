# WAP to check whether the year is a leap year or not

'''
Leap Year:
1. Leap year repeats after every 4 years (year % 4 == 0)
                and
2. For Century Years (100, 200, 400, 800...1600,1800,2000,2400)
    a. Not all century years are leap year (year % 100 != 0)
                or
    b. Century year that repeats after every 400 years are Leap Year (year % 400 == 0)
'''

year = int(input("Enter a year: "))

if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(f"Year = {year} is a Leap Year")
    
else :
    print(f"Year = {year} is not a Leap Year")