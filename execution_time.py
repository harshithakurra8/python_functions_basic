# Write a Python program to get the execution time of a Python method.

import time
def sample_method():
    print("Starting task...")
    time.sleep(2)  
    print("Task finished.")

start_time = time.time()

sample_method()

end_time = time.time()

execution_time = end_time - start_time

print(f"Execution time: {execution_time:.2f} seconds")
