# Right Angle Triangle Opposite

n = int(input("Enter a number: "))

i = 1
# ROW
while(i<=n):
    # SPACE
    sp = 1
    while(sp <= n-i):
        print(" ",end="")
        sp += 1
    
    # STAR
    j = 1
    while(j <= i):
        print("*",end=" ")
        j += 1

    # New Line
    print()
    i += 1
