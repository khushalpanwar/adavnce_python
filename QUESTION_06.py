#   Write a Python program to read a file line by line and store it into a list.

def read_file_into_list(file_path):
    lines_list = []
    try:
        with open(file_path, 'r') as file:
            lines_list = file.readlines()
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except IOError:
        print(f"An error occurred while reading the file {file_path}.")
    
    return lines_list

# Replace 'example.txt' with the path to your file
file_path = 'example.txt'
lines = read_file_into_list(file_path)
print(lines)
