'''
WAP to accept marks of 5 subject  display sum and average
based on average display grades
1. average between 100 and 90 -> A Grade
2. average between 89 and 70 -> B Grade
3. average between 69 and 50 -> C Grade
4. average between 49 and 35 -> D Grade
5. Below 35 -> Fail
'''
m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))

sum = (m1+m2+m3+m4+m5)
avg = sum / 5

print(f"Sum = {sum}, average = {avg}")

if avg >=90 :
    print("A Grade")
elif avg >= 70 : 
    print("B Grade")
elif avg >= 50 : 
    print("C Grade")
elif avg >= 35 : 
    print("D Grade")
else:
    print("FAIL")