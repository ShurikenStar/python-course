import math
num=float(input("Enter a number: "))
if num >= 0:
    print(f"Square root: {math.sqrt(num)}")
else:
    print("Square root is not defined for negative numbers.")
if num > 0:
    print(f"Logarithm of {num}: {math.log(num)}")
else:
    print("Logarithm is only defined for positive numbers.")
print(f"Sine: {math.sin(num)}")
