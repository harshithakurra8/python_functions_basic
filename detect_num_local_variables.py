#  Write a Python program to detect the number of local
#  variables declared in a function

def abc():
    x=1
    y=2
    str1='hello'
print(abc.__code__.co_nlocals)
