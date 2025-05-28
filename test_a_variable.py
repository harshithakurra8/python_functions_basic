#  Write a Python program to test if a variable is a list
#  or tuple or a set

x = ('tuple',False, 3.2 ,7)
if type(x) is list:
    print("'x' is list")
elif type(x) is set:
    print("'x' is set")
elif type(x) is tuple:
    print("'x' is tuple")
else:
    print("Neither a list nor a tuple nor set")