#  Write a Python program to count the frequency of words in a file.

from collections import Counter
import re

def count_word_frequency(file_path):
    word_freq = Counter()
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Remove non-alphanumeric characters and convert to lower case
                words = re.findall(r'\b\w+\b', line.lower())
                word_freq.update(words)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except IOError:
        print(f"An error occurred while reading the file {file_path}.")
    
    return word_freq

# Replace 'example.txt' with the path to your file
file_path = 'example.txt'
word_frequencies = count_word_frequency(file_path)

print("Word frequencies in the file:")
for word, freq in word_frequencies.items():
    print(f"{word}: {freq}")
