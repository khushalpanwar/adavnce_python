#  Write a Python program to read a file line by line store it into a variable.

def read_file_into_variable(file_path):
    content = ""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except IOError:
        print(f"An error occurred while reading the file {file_path}.")
    
    return content

# Replace 'example.txt' with the path to your file
file_path = 'example.txt'
file_content = read_file_into_variable(file_path)
print(file_content)
