#  Write a Python program to write a list to a file.

def write_list_to_file(file_path, data_list):
    try:
        with open(file_path, 'w') as file:
            for item in data_list:
                file.write(f"{item}\n")
        print(f"List successfully written to {file_path}")
    except IOError:
        print(f"An error occurred while writing to the file {file_path}")

# Example list
data_list = ['apple', 'banana', 'cherry', 'date']

# Replace 'output.txt' with the desired file path
file_path = 'output.txt'

# Call the function to write the list to the file
write_list_to_file(file_path, data_list)
