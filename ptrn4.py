'''
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
'''

n = int(input("Enter a number: "))

i = 1
while(i<=n):
    j = 1
    while(j<=n):
        if((i+j) % 2 == 0):
            print("0",end=" ")
        else:
            print("1",end=" ")
        j += 1      
    print()
    i += 1