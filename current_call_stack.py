#  Write a Python program to print the current call stack

import traceback
def f1():
    return abc()

def abc():
    traceback.print_stack()

f1()