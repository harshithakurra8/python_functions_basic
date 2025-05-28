#  Write a Python program to sum of three given integers.
#  However, if two values are equal sum will be zero

def sum(a, b, c):
   if a == b or b == c or c == a:
        return 0
   return a + b + c

a = int(input("Enter 1st no:"))
b = int(input("Enter 2nd no:"))
c = int(input("Enter 3rd no:"))

result = sum(a, b, c)
print("Result:",result)