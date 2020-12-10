# defines a function called add that takes two parameters, a and b. It returns the sum of a + b. I guess the advantage of this is that the result can be assigned to a variable. I tried this using print, but it didn't work. It only worked with 'return'.
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b
    # print(a + b)

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING: {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING: {a} / {b}")
    return a / b

print("Let's do some math with just functions.")

age = add(30, 5)
height = subtract(70, 6)
weight = multiply(10, 13)
iq = divide(100, 2)

print(f"Age: {age}\nHeight: {height}\nWeight: {weight}\nIQ: {iq}")

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

# (((4 / 2) * 6) / (((4 + 3) * 8) % 2)) + 16

top = ((4 / 2) * 6)
bottom = (((4 + 3) * 8) / 2)

def equation(a, b, c):
    print(f"DIVIDING: {a} by {b} then adding {c}")
    return a / b + c

equation_output = equation(top, bottom, 16)

print(f"Equation equals {equation_output}")