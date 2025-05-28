# Write a Python program to calculate the hypotenuse of a right angled triangle.

import math
a = float(input("Enter the length of side A: "))
b = float(input("Enter the length of side B: "))
hypotenuse = math.sqrt(a**2 + b**2)

print(f"The length of the hypotenuse is: {hypotenuse:.2f}")
