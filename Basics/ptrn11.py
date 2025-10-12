# K Pattern

n = int(input("Enter a number: "))

# Upper Half
i = n

# ROW
while(i >= 1):

    # STAR
    j = 1

    while( j <= i):
        print("*", end=" ")
        j += 1

    # Decrement 
    i -= 1
    # NEW LINE
    print()

# MIRROR OF UPPER HALF
# Lower Half


i = 2
# ROW
while(i <= n):

    # STAR
    j = 1

    while( j <= i):
        print("*", end=" ")
        j += 1

    # Increment
    i += 1
    # NEW LINE
    print()