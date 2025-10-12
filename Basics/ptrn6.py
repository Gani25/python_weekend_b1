# Right Angled Triangle
n = int(input("Enter a number: "))

# ROW
i = n

while i >= 1:
    # COLUMN
    j = 1
    while j <= i:
        print("*",end=" ")
        # Increase Column
        j += 1
    
    # Decrease ROW
    i -= 1
    # New Line
    print()