#Write a Python program to check whether a string is numeric


str='a123'
try:
    i=float(str)
    print("Numeric")
except(ValueError,TypeError):
    print("Not numeric")