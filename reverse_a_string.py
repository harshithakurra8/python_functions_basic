# 4. Write a Python program to reverse a string.
#  Sample String : "1234abcd"
#  Expected Output : "dcba4321

def reverse_string(s):
    return s[::-1]

user_input=input("Enter  a string to be reverse:")
reverse_string=reverse_string(user_input)

print("Reversed String:",reverse_string)