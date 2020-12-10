name = 'Joe Cardillo'
age = 35 # not a lie
height_in = 69 # inches
height_cm = height_in * 2.54
weight_lbs = 130 # lbs
weight_kilos = weight_lbs / 2.205
eyes = 'hazel'
teeth = 'white'
hair = 'brown'

print(f"Let's talk about {name}.")
print(f"He's {height_in} inches tall.")
print(f"His height in centimeters is {height_cm} cm.")
print(f"He's {weight_lbs} pounds heavy.")
print(f"Actually that's pretty light.")
print(f"His weight in kilograms is {weight_kilos:.4}.")
# Using the round function
print(f"His rounded weight in kilograms is {round(weight_kilos)}.")
print(f"he's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on how much coffee he drank.")

# this line is tricky, try to get it exactly right
total = age + height_in + weight_lbs
print(f"If I add {age}, {height_in}, and {weight_lbs} I get {total}.")
