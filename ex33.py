numbers = []

def new_list(new, increment):
    i = 0
    while i < new:
        print(f"At the top i is {i}")
        numbers.append(i)
        i += increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)

# Written using for loop only
numbers = []

for i in range(0, 6):
    print(f"At the top i is {i}")
    numbers.append(i)
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)