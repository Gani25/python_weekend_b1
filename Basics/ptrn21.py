'''
n = 4


4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
'''
n = int(input("Enter a number: "))
length = 2 * n - 1
i = 1
while(i <= length):

    j = 1
    while(j <= length):

        dr = abs(i - n)
        dc = abs(j - n)
        greatest = max(dr,dc)
        print(greatest + 1,end=" ")        
        j+=1
    i += 1
    print()