#  Write a Python program to convert all units of time into seconds

days = int(input("Enter number of days: "))
hours = int(input("Enter number of hours: "))
minutes = int(input("Enter number of minutes: "))
seconds = int(input("Enter number of seconds: "))

total_seconds = (
    days * 24 * 60 * 60 +     
    hours * 60 * 60 +        
    minutes * 60 +            
    seconds                   
)


print("Total time in seconds is:", total_seconds)