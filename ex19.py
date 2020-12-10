# creating a function called cheese_and_crackers that takes two arguments.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses.")
    print(f"You have {boxes_of_crackers} boxes of crackers.")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
# calls this function, and passes two integers into it:
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
# sets two variables to integers
amount_of_cheese = int(input("How many cheeses? "))
amount_of_crackers = int(input("How many crackers? "))

# calls function and passes in the variables we just set
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
# calls function and passes two arguments in the form of addition
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
# calls function and passes in two arguments that are a combination of variables and integers added together
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# creating my own function
def my_function(book, music, food):
    print(f'my favorite book is {book}.')
    print(f'I like listening to {music}')
    print(f'I love to eat {food}')

# call the function and pass three arguments to it
my_function("crime and punishment", "philip glass", "pizza")

# set three variables to something using the input function
favorite_book = input("What's your favorite book? ")
favorite_music = input("What's your favorite music? ")
favorite_food = input("What's your favorite food? ")

# call the function again, passing in these new variables
my_function(favorite_book, favorite_music, favorite_food)

from sys import argv
script, book, music, food = argv
my_function(book, music, food)
