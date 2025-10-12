# CROWN
n = int(input("Enter a number: "))

# ROW
i = 1
while(i <= n):

    # LEFT STAR
    j = 1
    while(j <= i):
        print("*",end=" ")
        j += 1
    
    sp = 1
    while(sp <= 2 * (n - i) - 1):
        print(" ",end=" ")
        sp += 1
    
    # RIGHT STAR
    j = 1
    while(j <= i):
        if (j<n):
            print("*",end=" ")
        j += 1
    
    # NEW LINE
    print()
    # Move to New Row
    i += 1