### Problem **3: Append new string in the middle of a given string**

# Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.

s1 = "Ault"
s2 = "Kelly"

middle_index = len(s1) // 2  # Calculate the middle index of s1

s3 = s1[:middle_index] + s2 + s1[middle_index:]  # Concatenate s1[:middle_index], s2, and s1[middle_index:]

print(s3)
