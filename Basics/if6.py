'''
Display statement based on below criteria
1. if number is divisible by 3 -> FIZZ
2. if number is divisible by 5 -> BUZZ
3. if number is divisible by 3 and 5 both -> FIZZBUZZ
4. if number is not divisible by 3 and 5 both -> Not Divisible
'''

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FIZZBUZZ")
elif num % 3 == 0:
    print("FIZZ")
elif num % 5 == 0:
    print("BUZZ")
else:
    print("Not Divisible")