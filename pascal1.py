'''
n = 5
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
'''

n = int(input("Enter a number: "))

i = 1
while(i <= n):

    # SPACE
    sp = 1
    while sp <= n-i:
        print(" ",end="")
        sp += 1
    
    pascal_number = 1
    j = 1
    while(j <= i):
        print(pascal_number,end=" ")
        pascal_number = pascal_number * (i - j)//j
        j += 1
    i += 1
    print()