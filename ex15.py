# imports argv module from sys
from sys import argv

# the two argv arguments
script, filename = argv

# Using only input instead of argv
# filename = input("Enter the filename: ")

# Opens the filename you gave when executing the script
txt = open(filename)

# prints a line
print(f"Here's your file {filename}:")

# The read() function opens the filename that's set to the txt variable
print(txt.read())

print("Type the filename again:")
txt.close()

# prompt to input the filename again
file_again = input("> ")

# sets variable txt_again equal to the open function with one parameter: the variable file_again
txt_again = open(file_again)

# prints the content of the example15_sample.txt file by calling the read function on the txt_again variable.
print(txt_again.read())
txt_again.close()