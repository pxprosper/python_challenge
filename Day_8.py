# Project 8: Count lines and words in a file

# Ask for the file name
filename = input("Enter the name of the text file (e.g., sample.txt): ")

try:
    with open(filename, "r") as file:
        lines = file.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)

        print(f"Lines: {line_count}")
        print(f"Words: {word_count}")

except FileNotFoundError:
    print("The file was not found. Please check the name and try again.")
