#   Write a Python program to copy the contents of a file to another file.

def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
            dest.write(src.read())
        print(f"File copied successfully from {source_file} to {destination_file}")
    except FileNotFoundError:
        print(f"One of the files {source_file} or {destination_file} does not exist.")
    except IOError:
        print(f"An error occurred while copying from {source_file} to {destination_file}.")

# Replace 'source.txt' and 'destination.txt' with your file paths
source_file = 'source.txt'
destination_file = 'destination.txt'

# Call the function to copy the contents of source_file to destination_file
copy_file(source_file, destination_file)
