# print("How old are you?", end=' ')
# age = input()
# print("What's your favorite color?", end=' ')
# color = input()
# print("How tall are you?", end=' ')
# height = input()
# print("How much do you weigh?", end=' ')
# weight = input()

# Reformatting the above:
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")
color = input("What's your favorite color? ")
print(f"So, you're {age} years old, {height} tall and {weight} heavy.")
print("Your favorite color is: ", color)

# You don't need the end=' ' thing if you're doing it this way:
food = input("One more question. What's your favorite food: ")
print("Your favorite food is", food)

print("Let's convert a string to an integer. Type a number:", end=' ')
number = int(input())
print("Your number is:", number)