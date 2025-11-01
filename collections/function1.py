#1.  WAP to create a function which accept 2 number as parameter
# and then return addition of 2 numbers
#2.  WAP to create a function which accept 2 number as parameter
# and then return exponent of 2 numbers
#3.  WAP to create a function which accept 2 number as parameter
# and then return multiplication of 2 numbers
#4. WAP to create a function which takes input of 2 numbers
# and returns addition, multiplication, exponent

def addition(n1,n2):
    return n1+n2
def exponent(a,b):
    return a ** b
def multiplication(n1,n2):
    return n1*n2

def square_list(n):
    squares = []
    for i in range(1,n+1):
        squares.append(i*i)
    
    return squares
    
    

# It will return addition, exponent, multiplication
def myFun():
    n1 = int(input("Enter number 1: "))
    n2 = int(input("Enter number 2: "))

    return addition(n1,n2), exponent(n1,n2), multiplication(n1,n2), square_list(n1)


results = myFun()
print("Type of result =",type(results))
print("Value of result =",results)

print("Addition = ",results[0])
print("Power = ",results[1])
print("Multiplication = ",results[2])

addResult,powerResult,multiplyResult, sq_list= myFun()

print("After spreading tupple into variable")
print("Addition = ",addResult)
print("Power = ",powerResult)
print("Multiplication = ",multiplyResult)
print("Squares of Numbers = ",sq_list)
