#Write a Python program to test whether a passed letter is a vowel or not

def vowel(char):
    vowels="aeiou"
    return char in vowels
print(vowel('h'))
print(vowel("a"))