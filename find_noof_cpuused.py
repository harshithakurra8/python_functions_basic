#  Write a Python program to find out the number of CPUs
#  using

import multiprocessing

cpu_count=multiprocessing.cpu_count()
print(cpu_count)