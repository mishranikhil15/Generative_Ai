# Write a Python function that takes a string and returns the string in reverse order.

# 5. **String Reversal**: Write a Python function that takes a string and returns the string in reverse order.
#     - *Input*: "Python"
#     - *Output*: "nohtyP"

def ReverseString(str) : 
    return str[::-1]


str="Nikhil"
reverseStr=ReverseString(str)
print(reverseStr)