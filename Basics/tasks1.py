'''
n = 6
* * * * * * * * * * * *
* * * * *     * * * * *
* * * *         * * * *
* * *             * * *
* *                 * *
*                     *
* *                 * *
* * *             * * *
* * * *         * * * *
* * * * *     * * * * *
* * * * * * * * * * * *
'''

n = int(input("Enter a number: "))

# UPPER HALF
# ROWS
i = 1
while(i <= n):
    # LEFT STAR
    j = 1
    while(j <= n-i+1):
        print("*",end=" ")
        j += 1
    # SPACE
    sp = 1
    while(sp <= 2*(i-1)):
        print(" ",end=" ")
        sp += 1
     # RIGHT STAR
    j = 1
    while(j <= n-i+1):
        print("*",end=" ")
        j += 1
    
    # ROW INCREMENT
    i += 1
    # Move Cursor To Next ROW
    print() 

# LOWER HALF
# ROWS
i = n - 1
while(i >= 1):
    # LEFT STAR
    j = 1
    while(j <= n-i+1):
        print("*",end=" ")
        j += 1
    # SPACE
    sp = 1
    while(sp <= 2*(i-1)):
        print(" ",end=" ")
        sp += 1
     # RIGHT STAR
    j = 1
    while(j <= n-i+1):
        print("*",end=" ")
        j += 1
    
    # ROW DECREMENT
    i -= 1
    # Move Cursor To Next ROW
    print() 