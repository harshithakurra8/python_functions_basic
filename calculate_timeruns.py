#  Write a Python program to calculate the time runs
#  (difference between start and current time) of a program

import time
start=time.time()
time.sleep(2)
current=time.time()
difference=current-start
print(f"The program ran for {difference:.2f}seconds")