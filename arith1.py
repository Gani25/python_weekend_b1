# WAP to understand arithmetic operators

n1 = 11
n2 = 3

result = n1 ** n2 # 11 to the power 3 (11 cube)
print("1. ** -> Raise To (Exponent/Power)")
# 11 raise to 3 = 1331
print(n1," raise to ",n2," = ",result)
# Formatted String -> fstring -> open only quotes 1 time
print(f"{n1} raise to {n2} = {result}")

print()
print("2. * -> multiply")
result = n1 * n2
print(f"{n1} * {n2} = {result}")

print()
print("3. / -> Divide -> Decimal Quotient")
result = n1 / n2
print(f"{n1} / {n2} = {result}")

print()
print("4. // -> Divide -> Integer Quotient")
result = n1 // n2
print(f"{n1} // {n2} = {result}")

print()
print("5. % -> Modulus (Gives Remainder)")
result = n1 % n2
print(f"{n1} % {n2} = {result}")

print()
# addition and subtraction