# Pyramid
n = int(input("Enter a number: "))

# ROW
i = n

while(i >= 1):

    # SPACE
    sp = 1
    while(sp <= n-i):
        print(" ",end=" ")
        sp += 1
    
    # STAR
    j = 1
    while(j <= (2 * i - 1)):
        print("*",end=" ")
        j += 1
    
    # NEW LINE
    print()
    i -= 1