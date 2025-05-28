#Write a Python program to convert the distance (in feet) to inches, yards, and miles

feet = float(input("Enter distance in feet: "))
inches = feet * 12
yards = feet / 3
miles = feet / 5280
print("Distance in inches:", inches)
print("Distance in yards :", yards)
print("Distance in miles :", miles)
