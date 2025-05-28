# Write a Python program to convert height (in feet and inches) to centimeters.


feet = int(input("Enter height in feet: "))
inches = int(input("Enter remaining inches: "))

total_inches = feet * 12 + inches

centimeters = total_inches * 2.54
print(f"Your height is {centimeters:.2f} centimeters.")
