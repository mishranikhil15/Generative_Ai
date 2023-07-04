# 1. **File I/O**: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.
#     - *Input*: A text file named "input.txt" with the content "Hello world"
#     - *Output*: A text file named "output.txt" with the content "Number of words: 2"

def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            word_count = len(content.split())
        return word_count
    except FileNotFoundError:
        return -1

def write_word_count(file_path, word_count):
    with open(file_path, 'w') as file:
        file.write(f"Number of words: {word_count}")

# Input file path and name
input_file_path = "input.txt"

# Output file path and name
output_file_path = "output.txt"

# Count words in the input file
word_count = count_words(input_file_path)

# Write the word count to the output file
write_word_count(output_file_path, word_count)

# Print the word count to the console
print(f"Number of words: {word_count}")

