#  Write a Python program to read first n lines of a file.


def read_first_n_lines(file_path, n):
    try:
        with open(file_path, 'r') as file:
            for i in range(n):
                line = file.readline()
                if line == '':
                    # End of file reached before n lines
                    break
                print(line, end='')
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except IOError:
        print(f"An error occurred while reading the file {file_path}.")

# Replace 'example.txt' with the path to your file and 5 with the number of lines you want to read
file_path = 'example.txt'
n = 5
read_first_n_lines(file_path, n)
