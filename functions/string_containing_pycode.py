# . Write a Python program to execute a string containing
#  Python code

code = """
def greet(name):
    print(f"Hello, {name}!")

greet("Joe")
"""

exec(code)
