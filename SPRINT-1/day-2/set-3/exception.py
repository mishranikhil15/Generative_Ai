# 2. **Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
#     - *Input*: 5, 0
#     - *Output*: "Cannot divide by zero."

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."

# Input numbers
num1 = 5
num2 = 0

# Divide the numbers and handle exceptions
division_result = divide_numbers(num1, num2)

# Print the result or error message
print(division_result)
