#  Write a Python program to list the special variables used
#  within the language


def list_special_variables():
    special_vars = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
    for var in special_vars:
        print(var)

list_special_variables()