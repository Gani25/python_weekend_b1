n = int(input("Enter a number: "))

i = 1

while(i<=n):

    j = 1
    while(j <= n):
        if(i == 1 or j == 1 or j == n or i == n):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        
        j += 1
    
    # New Line
    print()
    # Increment ROW
    i += 1