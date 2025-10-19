# Perimiter of rectangle - using function
# 2 * (l + b)

def perimeter_of_rectangle(length, breadth):
    print(f"Len of rectangle = {length}")
    print(f"Breadth of rectangle = {breadth}")

    perimeter = 2 * (length + breadth)

    print(f"Perimeter of rectangle = {perimeter}")

l = float(input("Enter length of rectangle: ")) 
b = float(input("Enter breadth of rectangle: ")) 


perimeter_of_rectangle(breadth=b,length=l)