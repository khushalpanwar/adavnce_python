#     Write a python program to find the longest words.

def find_longest_words(file_path):
    longest_words = []
    max_length = 0
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    word_length = len(word)
                    if word_length > max_length:
                        max_length = word_length
                        longest_words = [word]
                    elif word_length == max_length:
                        longest_words.append(word)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except IOError:
        print(f"An error occurred while reading the file {file_path}.")
    
    return longest_words

# Replace 'example.txt' with the path to your file
file_path = 'example.txt'
longest_words = find_longest_words(file_path)
print("The longest words are:")
for word in longest_words:
    print(word)
