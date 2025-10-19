# Area of cylinder
# 2 pi r h

r = float(input("Enter radius of a cylinder in cm: ")) 
h = float(input("Enter height of a cylinder in cm: ")) 


def area_of_cylinder(radius:float, height:float,pi:float = 3.14):
    area = 2 * pi * radius * height
    print(f"Radius of cylinder = {radius}")
    print(f"Height of cylinder = {height}")
    print(f"Area of a cylinder = {area}")


area_of_cylinder(r,h)

'''
1. Recurssion
2. Multiple Args --
3. kwargs
4. Function which returns multiple values
'''