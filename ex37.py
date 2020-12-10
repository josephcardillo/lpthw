# and
# assert - https://docs.python.org/3.7/reference/simple_stmts.html#the-assert-statement
    # asserts something is true, and if not, throws assertion error

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
death = False
def live_or_die():
    while death == False:
        print("You drank to much coffee.")
        print("Will you drink some more?")
        more_coffee = input("> ")
        if "yes" in more_coffee:
            print("Now you've done it. Goodbye!")
            break
        elif "no" in more_coffee:
            print("Good choice.")
        else:
            print("I don't understand that.")

health_check()

# as - part of the with statement
    # https://docs.python.org/3.7/whatsnew/2.6.html#pep-343-the-with-statement

with open("test.txt", 'r') as file:
    for line in file:
        stripped = line.strip()
        new_line = stripped + ' wtf'
        print(new_line)


