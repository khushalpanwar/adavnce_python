#   Write a Python program to read an entire text file.

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except IOError:
        print(f"An error occurred while reading the file {file_path}.")

# Replace 'example.txt' with the path to your file
file_path = 'example.txt'
read_file(file_path)
