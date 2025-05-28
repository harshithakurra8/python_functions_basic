# . Write a Python program to add trailing and leading
#  zeroes to a string

original = "123"
leading_zeros=original.zfill(6)
trailing_zeros=original+"000"
combined=leading_zeros+"000"

print("Original:",original)
print("Leading Zeros of a string:",leading_zeros)
print("Trailing Zeros of a string:",trailing_zeros)
print("Combined:",combined)
