# Cross Pattern X
n = int(input("Enter a number: "))

i = 1

while(i <= n):

    j = 1
    while(j <= n):
        if(i == j or i+j == n+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        
        j += 1
        
    print()
    i += 1