#  Write a Python program to check whether an integer fits
#  in 64 bits

int = 30
if int <= 63:
   print((-2 ** 63).bit_length())
   print((2 ** 63).bit_length())