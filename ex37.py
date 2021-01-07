# and
# assert - https://docs.python.org/3.7/reference/simple_stmts.html#the-assert-statement
    # asserts something is true, and if not, throws assertion error
    # https://www.programiz.com/python-programming/assert-statement

coffee = True
sleep = False

def health_check():
    if not coffee and sleep:
        print("You can survive just on sleep.")
    elif coffee and not sleep:
        print("You need coffee today.")
        drink_coffee()
    elif coffee and sleep:
        print("You will be extra productive today.")
    else:
        print("Good luck staying awake today.")

def drink_coffee():
    print("How many cups of coffee will you drink?")
    cups = int(input('> '))
    assert cups >= 1,"Sorry, that's not enough coffee to get you going."
    if  cups <= 3:
        print("That seems reasonable.")
    elif cups > 3:
        print("Are you hoping to have a heart attack?")
        live_or_die()
    else:
        print("I don't understand what that means.")

# break statement

def live_or_die():
    death = False
    while death == False:
        print("You drank to much coffee.")
        print("Will you drink some more?")
        more_coffee = input("> ")
        if "yes" in more_coffee:
            print("Now you've done it.")
            print(f"You should eat an {Fruits.a} instead.")
            print(f"And maybe a {Fruits.b}, too.")
            print("Goodbye!")
            break
        elif "no" in more_coffee:
            print("Good choice.")
            death = True
        else:
            print("I don't understand that.")

# class - https://docs.python.org/3.7/tutorial/classes.html
    # This is a very simply way to incorporate classes, but for the purpose of learning:

class Fruits:
    a = "Apple"
    b = "Banana"
    c = ["orange", "pineapple", "watermelon"]
    d = ["dates", "apple", "banana", "pineapple", "mange", "watermelon"]

# del - https://docs.python.org/3.7/tutorial/datastructures.html#the-del-statement

# del d[0] - deletes element at 0 index
# del d[0:4] - deletes elements at from index 0 to 3
# del d[:] - deletes everything in list

def list_fruits(f):
    for fruit in f:
        print(fruit)

# after importing the function into python
# from ex37 import *

# >>> list_fruits(Fruits.c)
# orange
# pineapple
# watermelon

# Otherwise, if I do:
# import ex37
# I need to do this to list them:
# >>> ex37.list_fruits(ex37.Fruits.c)
# orange
# pineapple
# watermelon

# continue - https://docs.python.org/3.7/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops


def weather():
    outside = True
    while outside == True:
        outside = input("Are you outside or inside? > ")
        if outside == "outside":
            outside = True
            continue
        elif outside == "inside":
            print("Just in time because a terrible storm is coming.")
            outside = False
        else:
            print("Try again.")
            outside = True
            continue

def print_even_num():
    for num in range(2, 10):
        if num % 2 == 0:
            print("You found an even number:", num)
            continue
        print(f"{num} is not even.")

def find_even_num():
    num = int(input("Enter a number: > "))
    if num % 2 != 0:
        print("Not an even number.")
        find_even_num()
    else:
        print(f"Yay! You found an even number: {num}")

# as - part of the with statement
    # https://docs.python.org/3.7/whatsnew/2.6.html#pep-343-the-with-statement
# with - https://docs.python.org/3.7/whatsnew/2.6.html#pep-343-the-with-statement

def with_statement():
    with open("test.txt", 'r') as file:
        for line in file:
            stripped = line.strip()
            new_line = stripped + ' yo.'
            print(new_line)

# except statement - https://docs.python.org/3.7/tutorial/errors.html

def integer_test():
    while True:
        try: # try this block. If an exception, go to except.
            num = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Exception: Oops! That was no valid number. Try again...")
        finally:
            print("This will print regardless of whether the 'Try' statement produces an exception.")
# exec - https://docs.python.org/3.7/library/functions.html#exec
# Run a string as python

# >>> program = 'a = 5\nb = 10\nprint("Sum of a and b is:", a + b)'
# >>> exec(program)
# Sum of a and b is: 15

# finally - https://docs.python.org/3.7/reference/compound_stmts.html#finally
# "If finally is present, it specifies a ‘cleanup’ handler."
# https://docs.python.org/3.7/tutorial/errors.html
    # Defining Clean-up Actions

# global - https://docs.python.org/3.7/reference/simple_stmts.html#the-global-statement

# Lambda expressions - https://docs.python.org/3.7/tutorial/controlflow.html#lambda-expressions

def make_incrementor(n):
    return lambda x: x + n

# >>> f = make_incrementor(2)
# >>> f(3)
# 5

# pass statement - https://docs.python.org/3.7/tutorial/controlflow.html#pass-statements
# The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action.

def pass_statement():
    while True:
        pass # busy - wait for keyboard interrupt (ctrl + c)

# raise - raising exceptions
# https://docs.python.org/3.7/tutorial/errors.html#raising-exceptions

def raise_exception():
    try:
        raise NameError('HiThere')
    except NameError:
        print('An exception flew by!')
        raise

# yield statement - https://docs.python.org/3.7/reference/simple_stmts.html#yield
# yield expression - https://docs.python.org/3.7/reference/expressions.html#yieldexpr
# https://www.python.org/dev/peps/pep-0255/

def gen():  # defines a generator function
    yield 123

def fib():
    a, b = 0, 1
    while 1:
       yield b
       a, b = b, a+b

# decorator @ - https://docs.python.org/3.7/reference/compound_stmts.html#function
# # https://docs.python.org/3.7/glossary.html#term-decorator

# find_even_num()
# find_even_num()
# health_check()
# weather()
# with_statement()
# integer_test()
# pass statement()
# raise_exception()
