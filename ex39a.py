# https://docs.python.org/3.7/library/stdtypes.html#typesmapping

states = {
    'New Jersey': 'NJ',
    'Pennsylvania': 'PA',
    'New York': 'NY',
    'Maryland': 'MD',
    'Deleware': 'DE'
}

cities = {
    'NJ': 'Newark',
    'PA': 'Philadelphia',
    'NY': 'Albany',
    'MD': 'Baltimore',
    'DE': 'Dover',
}

# print("New Jersey has the following cities: ", cities['NJ'])
# print("New Jersey has the following city: ", cities['NJ'])

# print("The abbreviation for New Jersey is: ", states['New Jersey'])

# print all the abbreviations
# for state, abbrev in list(states.items()):
#     print(f"{state} is abbreviated: {abbrev}")

# print all the cities
# for state, city in list(cities.items()):
#     print(f"{city} is in {state}.")

# check if Newark is in city list
# if 'Newark' in cities.values():
#     print('Newark exists')
# else:
#     print("Newark doesn't exist")

print(list(states))
print(len(cities))

