n = int(input("Enter a number: "))

# ROW
i = 1
while(i<=n):

    # SPACE
    sp = 1
    while(sp <= n - i):
        print(" ",end=" ")
        sp += 1
    
    # STAR
    j = 1
    while(j <= n):
        print("*",end=" ")
        j += 1
    
    # NEW LINE
    print()
    # Increment Row 
    i += 1