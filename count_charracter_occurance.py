# . Write a Python program to count the number occurrence of
#  a specific character in a string

text = input("Enter a string:")
char = input("Enter a specific character to count:")

count=text.count(char)
print(f"The character '{char}' appears {count} times in the string.")