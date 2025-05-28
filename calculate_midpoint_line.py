# . Write a Python program to calculate midpoints of a line

x1 = float(input("Enter x-coordinate of the first point: "))
y1 = float(input("Enter y-coordinate of the first point: "))

x2 = float(input("Enter x-coordinate of the second point: "))
y2 = float(input("Enter y-coordinate of the second point: "))

mid_x = (x1 + x2) / 2
mid_y = (y1 + y2) / 2


print(f"The midpoint of the line is: ({mid_x}, {mid_y})")
