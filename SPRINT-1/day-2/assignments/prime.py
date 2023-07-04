# Write a Python function that checks whether a given number is a prime number.

def is_prime_number(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

# Test the function
number = 14
if is_prime_number(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
