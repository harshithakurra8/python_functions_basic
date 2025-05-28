#  Write a Python program to calculate the sum of the digits
#  in an integer

number = int(input("Enter an integer: "))
number = abs(number)
digit_sum = 0

while number > 0:
    digit = number % 10       
    digit_sum += digit        
    number = number // 10     

print("The sum of the digits is:", digit_sum)
