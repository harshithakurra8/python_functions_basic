# Write a Python program to prove that two string
#  variables of same value point same memory location

str1 = "Hello"
str2 = "Hello"
print("Memory Location of string=",hex(id(str1)))
print("Memory location of string=",hex(id(str2)))