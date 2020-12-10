# import sys module. This is different than what we've previously done. Previously were saying "from sys import argv".
import sys
# I guess since we didn't import argv, we are calling argv by doing sys.argv
script, encoding, error = sys.argv

# defining a function named main, and passing it three variables.
def main(language_file, encoding, errors):
    line = language_file.readline() # read the first line of the file, and assign it to the line variable

    if line: # if statement... if line is... true?
        print_line(line, encoding, errors) # calls print_line function which hasn't been defined yet, passes three arguments to it.
        return main(language_file, encoding, errors) # calls main function that was already defined

# defines function named print_line, passes it three arguments. It doesn't matter that line is defined within another function, because this function is called with the 'main' function.
def print_line(line, encoding, errors):
    print(">>>> print_line", repr(line), encoding, errors)
    # strip returns a copy of the sequence with the specified leading and trailing bytes removed. In this case, it just removes any blank space at the beginning and end. I guess, more specifically, strips the \n character
    # https://docs.python.org/3.7/library/stdtypes.html
    next_lang = line.strip()
    # takes the stripped line, or the next_lang, and runs encode function on it
    # passes two args, encoding and errors. we specify errors when we run the script, because it's one of the argvs. same with encoding.
    # https://docs.python.org/3.7/library/stdtypes.html
    # encode - Return an encoded version of the string as a bytes object.
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # decode - Return a string decoded from the given bytes. Default encoding is 'utf-8'
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    print(raw_bytes, "<===>", cooked_string)
    print("<<<< exit print_line")

# opens languages.txt file encoded using utf-8
languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)