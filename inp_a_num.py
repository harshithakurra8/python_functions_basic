#  Write a Python program to input a number, if it is not a
#  number generate an error message

while True:
    try:
        a= int(input("Enter a number:"))
        break

    except ValueError:
        print("This is not a number.Try again....")
