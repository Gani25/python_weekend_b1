# WAP to print table of n till x iteration using functions
# n = 6, x = 15

def multiply(n1,n2):
    result = n1 * n2 

    print(f"{n1} * {n2} = {result}")



n = int(input("Enter Number To Display Table: "))
x = int(input("Enter Number Of Iteration: "))

for i in range(1,x+1):
    multiply(n,i)
