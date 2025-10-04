# Right Angled Triangle
n = int(input("Enter a number: "))

# ROW
i = 1

while i <= n:
    # COLUMN
    j = 1
    while j <= i:
        print("*",end=" ")
        # Increase Column
        j += 1
    
    # Increase ROW
    i += 1
    # New Line
    print()