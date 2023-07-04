### Problem **4: Arrange string characters such that lowercase letters should come first**

# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

str1 = "PyNaTive"

lowercase_letters = ""
uppercase_letters = ""

for char in str1:
    if char.islower():
        lowercase_letters += char
    else:
        uppercase_letters += char

arranged_string = lowercase_letters + uppercase_letters

print(arranged_string)
