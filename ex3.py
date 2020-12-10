print("I will now count my chickens:")
# Counts number of hens
print("Hens", 25 + 30 / 6)
# Counts number of roosters. Calculates 25 * 3 which is 75. 75 modulo 4 is 3, because it takes 75 / 4, which is 72, then spits out the remainder, which is 3. 100 - 3 is 97.
print("Roosters", 100 - 25 * 3 % 4)

print("Now I will count the eggs:")

# order of operations does mult and div first. 4 % 2 is 0. 1 / 4 is 0.25. 3 + 2 + 1 - 5 - 0.25 + 6 = 6.75
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
print("Is it true that 3 + 2 < 5 - 7?")

# calculates left and right separately. 3 + 2 = 5 and 5 - 7 - -2. 5 is not less than 2, so this evaluates to false.
print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")

# Yes, 5 is greater than 2, so this evaluates to true.
print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= 2)