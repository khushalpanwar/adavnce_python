# Write a Python program to append text to a file and display the text.

def append_and_read_file(file_path, text_to_append):
    # Append text to the file
    try:
        with open(file_path, 'a') as file:
            file.write(text_to_append + '\n')
    except IOError:
        print(f"An error occurred while appending to the file {file_path}.")
        return

    # Read and display the content of the file
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content after appending:")
            print(content)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except IOError:
        print(f"An error occurred while reading the file {file_path}.")

# Replace 'example.txt' with the path to your file and 'Your text here' with the text you want to append
file_path = 'example.txt'
text_to_append = 'This is the appended text.'
append_and_read_file(file_path, text_to_append)
