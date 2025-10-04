n = int(input("Enter a number: "))

# ROW
i = 1
count = 1
while (i <= n):

    j = 1

    while(j <= n):
        print(count,end="\t")
        j += 1
        count += 1    
    # New Line
    print()
    i += 1