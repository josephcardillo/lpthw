# A string with four slots for variables
formatter = "{} {} {} {}"

# prints numbers 1 through 4 using the formatter variable above
print(formatter.format(1, 2, 3, 4))
# prints one two three for
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, True, False))
# Prints {} {} {} {} four times
print(formatter.format(formatter, formatter, formatter, formatter))
# Should print the poem on a single line
print(formatter.format(
    "It rained alot today",
    "but now it seems to be clearing up.",
    "According to the weather it might rain some more.",
    "that'd be ok."
))
