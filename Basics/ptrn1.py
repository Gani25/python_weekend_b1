# Patterns

n = int(input("Enter a number: "))

# ROW
i = 1
while(i <= n):

    # COLUMNS
    j = 1
    while(j <= n):
        print("*",end=" ")
        j = j + 1
    
    # Next Row
    print()
    i = i + 1

