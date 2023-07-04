# Write a Python function that calculates the factorial of a number.

def factorial(num):
    if num < 0:
        return None

    result = 1
    for i in range(1, num + 1):
        result *= i

    return result

# Test the function
number = 5
factorial_result = factorial(number)
print("Factorial of", number, "is:", factorial_result)
