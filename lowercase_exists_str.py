# . Write a Python program to check whether lowercase
#  letters exist in a string

str = "aFFGUUDUsfiIU"
print(any(c.lower() for c in str))