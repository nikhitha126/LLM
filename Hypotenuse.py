import math
def calculate():
    return math.sqrt(a**2 + b**2)
a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
hypotenuse = calculate()
print(f"The hypotenuse of the triangle is: {hypotenuse:.2f}")
