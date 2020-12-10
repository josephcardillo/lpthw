# Exit from Python.
# https://docs.python.org/3.7/library/sys.html
from sys import exit

# defines function called gold_room with no arguments.
def gold_room():
    print("This room is full of gold. How much do you take?")
    # assigns input from user to choice variable
    choice = int(input("> "))
    # this only gives you the choice to type 0 or 1 as a string. 
    # if "0" in choice or "1" in choice:
    if 0 <= choice <= 50: 
        print("Nice, you're not greedy, you win!")
        exit(0)
        # int then converts that to an integer
        # how_much = int(choice)
    # if you type anything but 0 or 1, you call the dead function, which passes in the string, then tacks on "Good job!" from this: print(why, "Good job!")
    # else:
        # dead("Man, learn to type a number.")
    
    # if what you typed was less than 50 you're not greedy and the game ends with "exit(0)"
    # if how_much < 50:
    # if choice < 50:
        # print("Nice, you're not greedy, you win!")
        # exit(0)
    # otherwise, if more than 50, call the dead function
    else:
        dead("You greedy bastard!")

# define a function called bear_room with no arguments
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    # bear_moved variable is set to False
    bear_moved = False

    # This creates an infinite loop.
    # while True:
    #     # print(f"Bear moved is {bear_moved}.")
    #     choice = input("> ") # prompts user for input
    #     # if user types "take honey"
    #     if choice == "take honey":
    #         # call dead function
    #         dead("The bear looks at you then slaps your face off.")
    #     # if user types "taunt bear" and bear_moved is... 
    #     # in looking at https://docs.python.org/3.7/library/stdtypes.html#list
    #     # it seems to indicate that "not x" means "if x is false, then True, else False". So in this case, not bear_moved implies, "if bear_moved is false", which it is, then True. That's the only thing that would make sense here.
    #     elif choice == "taunt bear" and not bear_moved:
    #         # print(f"bear_moved is {bear_moved}.")
    #         # print(f"not bear_moved is {not bear_moved}")
    #         print("The bear has moved from the door.")
    #         print("You can go through it now.")
    #         bear_moved = True
    #     elif choice == "taunt bear" and bear_moved:
    #         # print(f"bear_moved is {bear_moved}.")
    #         # print(f"not bear_moved is {not bear_moved}")
    #         dead("The bear gets pissed off and chews your leg off.")
    #     elif choice == "open door" and bear_moved:
    #         gold_room()
    #     else:
    #         print("I got no idea what that means.")

    # refactoring code
    choice = input("> ")
    if choice == "take honey":
        dead("The bear looks at you then slaps your face off.")
    elif choice == "taunt bear" and not bear_moved:
        print("The bear has moved from the door.")
        print("You can go through it now.")
        bear_moved = True
    elif choice == "taunt bear" and bear_moved:
        dead("The bear gets pissed off and chews your leg off.")
    elif choice == "open door" and bear_moved:
        gold_room()
    else:
        print("I got no idea what that means.")
        bear_room()

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which on do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()