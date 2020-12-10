from sys import exit

def start():
    print("You open the freezer and you're out of blueberries.")
    print("Will you go to store or back to bed?")
    choose_store()

def choose_store():
    answer = input("> ")
    if answer == "go to store":
        go_to_store()
    elif answer == "back to bed":
        print("You fell asleep and never woke up. You died from hunger.")
        exit(0)
    else:
        print("That's not an option. Try again.")
        choose_store()

def go_to_store():
    print("Will you go to Moms or TJs?")
    store = input("> ")
    if store == "TJs":
        get_a_cart()
    elif store == "Moms":
        print("Blueberries at Moms are too expensive.")
        print("You couldn't buy enough to feed your family so everyone died from hunger.")
    else:
        print("That store doesn't exist. Try again.")
        go_to_store()

def get_a_cart():
    print("Since it's the holidays there are a lot of people here and there are no shoppping carts left.")
    print("You see an elderly man unloading his cart at his car.")
    print("Do you ask him if you can use it when he's finished (wait) or throw his groceries out of his cart and steal it (steal)?")
    have_a_cart = False
    patience = False

    while have_a_cart == False:
        get_cart = input("> ")
        if get_cart == "wait" and not patience:
            print("He's taking a long time. Do you wait, or steal it?")
            patience = True
        elif get_cart == "wait" and patience:
            print("You are a patient soul. The old man is senile and rewards you with $100.")
            have_a_cart = True
            enter_store()
        elif get_cart == "steal":
            print("The elderly man is actully quite senile and he pulls a knife and kills you. The end.")
            exit(0)
        else:
            print("This is a binary world and that's not an option.")
            print("You must choose 'wait' or 'steal'.")

def enter_store():
    print("You make a b-line for the blueberries.")
    print("But you notice a very large man taking the last pack.")
    print("His cart is extremely full of blueberries.")
    print("Do you push him over (push) or ask an employee if there's any more in back (ask)?")
    have_blueberries = False
    patience = False

    while have_blueberries == False:
        last_straw = input("> ")
        if last_straw == "push" and not patience:
            print("Wrong decision. The man slams you into a pancake and eats you for lunch with blueberry jam.")
            exit(0)
        elif last_straw == "steal" and patience:
            print("You've successfully snagged a few bags.")
            print("Enough to feed the family for two days.")
            print("You leave the store in triumph.")
            have_blueberries = True
            exit(0)
        elif last_straw == "ask" and not patience:
            print("The employee is taking a very long time.")
            print("Do you try stealing a few bags from the large man?")
            print("Or do you wait?")
            patience = True
        elif last_straw == "wait" and patience:
            print("The employee comes back shortly after.")
            print(f"She gives you two boxes worth at at 10% discount")
            print("You rejoice, triumphant that you can feed your family for weeks.")
            have_blueberries = True
            exit(0)
        else:
            print("Invalid answer. Try again.")

start()
