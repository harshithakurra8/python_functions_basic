# . Write a Python program to compute the future value of a
#  specified principal amount, rate of interest, and a number of
#  years.
#  Test Data : amt = 10000, int = 3.5, years = 7
#  Expected Output : 12722.79

principal = 10000
rate = 3.5  
years = 7

future_value = principal *(1 +rate / 100) ** years
print(f"Future Value = {future_value:.2f}")