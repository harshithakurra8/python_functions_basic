# 19. Write a Python program to get a new string from a given
 #string where "Is" has been added to the front. If the given
#string already begins with "Is" then return the string unchanged

def modify_string(s):
    if s.startswith("Is"):
        return s
    else:
        return "Is"+s
user_input=input("Enter a word: ")
s=modify_string(user_input)
print("Modified String:",s)