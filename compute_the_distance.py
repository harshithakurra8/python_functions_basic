# Write a Python program to compute the distance between
#  the points (x1, y1) and (x2, y2)

import math

x1 , y1 = 4, 0
x2 , y2 = 6, 6

distance=math.sqrt((x2 - x1)**2 +(y2 - y1)**2)

print(f"Distance between the points ={distance:.2f}")