# 1. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."


def is_palindrome(word):
    # Remove any spaces and convert to lowercase
    word = word.replace(" ", "").lower()

    # Check if the word is equal to its reverse
    if word == word[::-1]:
        return f"The word {word} is a palindrome."
    else:
        return f"The word {word} is not a palindrome."


# Example usage
word = "madam"
result = is_palindrome(word)
print(result)
