
try:
    n1 = int(input("Enter numerator: "))
except ValueError as ve:
    print(ve)
try:
    n2 = int(input("Enter denominator: "))
except ValueError as ve:
    print(ve)

# try:
#     result = n1 / n2 
# except NameError as ne:
#     print("Name Error 1 ->",ne)
# except ZeroDivisionError as ze:
#     print("Zero Division Error ->",ze)


try:
    # file open
    result = n1 / n2
    # Problem 
except Exception as e:
    print("Error Aaya Hai ->",e)
else:
    print("Else running...")
finally:
    print("Finally running")
    # closing the resources

try:
    print(f"Division of {n1}, {n2} = {result}")
    
except NameError as ne:
    print("Name Error 2 ->",ne)

index = 5 

arr = [5,1,7,9,3]
try:
    
    print(arr[index])

except Exception as e:
    print(e)