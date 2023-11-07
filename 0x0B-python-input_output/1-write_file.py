#!/usr/bin/python3
def write_file(filename="", text=""):
    """Function that writes a string to a text file (UTF-8) and returns the number of characters written."""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)

if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
