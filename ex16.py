# from the sys module, import the argv object
from sys import argv
# just ask for the filename when running the script
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
# Shows a ? on the screen, and if you hit any key it continues. It's not set to any variable so it doesn't do anything.
input("?")

print("Opening the file...")
# Opens the file for writing.
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# truncate() empties the file
target.truncate()

print("Now I'm going to ask you for three lines.")

# prompts user for three lines, setting them to variables
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# target.write(line1)
# writes a new line to the file
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# if you want to consolidate this you need to use a format string instead, since the write function doesn't take more than one argument.
target.write(f'{line1}\n{line2}\n{line3}\n')

print("And finally, we close it.")
# closes file, or saves it
target.close()