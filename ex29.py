people = 30
cats = 20
dogs = 15

if people < cats and cats > people:
    print("Too many cats! The world is doomed!")
else:
    print("Not many cats! The world is saved!")

# if people > cats:
#     print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")
