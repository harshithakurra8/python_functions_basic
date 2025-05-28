#  Write a Python program to access a function inside a
#  function

def outer_func(name):
    def inner_func():
        print(f"Hello,{name}!")

        inner_func()
outer_func("Joe")