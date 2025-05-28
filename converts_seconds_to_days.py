#  Write a Python program to convert seconds to day, hour,
#  minutes and seconds

total_seconds = int(input("Enter time in seconds: "))
days = total_seconds // (24 * 3600)
remaining_seconds = total_seconds % (24 * 3600)

hours = remaining_seconds // 3600
remaining_seconds %= 3600

minutes = remaining_seconds // 60

seconds = remaining_seconds % 60

print("Time is:")
print(days, "days")
print(hours, "hours")
print(minutes, "minutes")
print(seconds, "seconds")
