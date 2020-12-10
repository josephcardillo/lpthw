from sys import argv

script, input_file = argv

def print_all(f): # defines function called print_all that takes one argument, f, which I guess means 'file' in this case.
    print(f.read()) # read the contents of the 'file' or 'f'

def rewind(f): # define function and pass one argument, f
    f.seek(0) # uses beginning of file as starting reference point

def print_a_line(line_count, f): # define function that takes two arguments, line_count and f. f is the file.
    print(f.tell())
    print(line_count, f.readline(), end="") # line_count is just a line number. f.readline() will literally just read one line after another, each time it's run.

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
# current_line is equal to 1
print_a_line(current_line, current_file)

current_line += 1
# current_line is equal to 2
print_a_line(current_line, current_file)

current_line += 1
# current_line is equal to 3
# current line gets passed to the line_count arg in the print_a_line function
print_a_line(current_line, current_file)



