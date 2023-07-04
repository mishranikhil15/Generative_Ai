# Write a Python function that generates the first n numbers in the Fibonacci sequence.

def fibonacci(n):
    sequence = []
    if n <= 0:
        return sequence
    elif n == 1:
        sequence.append(0)
    elif n >= 2:
        sequence = [0, 1]
        while len(sequence) < n:
            next_number = sequence[-1] + sequence[-2]
            sequence.append(next_number)
    return sequence

# Test the function
n = 10
fibonacci_sequence = fibonacci(n)
print("Fibonacci sequence:", fibonacci_sequence)
