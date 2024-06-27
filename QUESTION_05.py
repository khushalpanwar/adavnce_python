#   Write a Python program to read last n lines of a file.

from collections import deque

def read_last_n_lines(file_path, n):
    try:
        with open(file_path, 'r') as file:
            # Use deque to keep only the last n lines
            last_n_lines = deque(file, maxlen=n)
            for line in last_n_lines:
                print(line, end='')
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except IOError:
        print(f"An error occurred while reading the file {file_path}.")

# Replace 'example.txt' with the path to your file and 5 with the number of lines you want to read
file_path = 'example.txt'
n = 5
read_last_n_lines(file_path, n)
