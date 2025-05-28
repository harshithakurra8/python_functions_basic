#  Write a Python program to convert an integer to binary
#  keep leading zeros.
#  Sample data : x=12
#  Expected output : 00001100
#  0000001100

x = 12
binary_8bit = format(x,'08b')
binary_10bit=format(x,'010b')
print("8-bit binary:",binary_8bit)
print("10-bit binary:",binary_10bit)