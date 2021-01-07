meal_plan = {
    "Monday": "tuna sandwiches",
    "Tuesday": "crackers and cheese",
    "Wednesday": "caesar salad",
    "Thursday": "spaghetti and meatballs",
    "Friday": "pizza"
}

def meals():
    for day, food in meal_plan.items():
        print(f"On {day}, I'll make {food}.")

meals()

meals = ["tuna sandwiches", "crackers and cheese", "caesar salad", "spaghetti and meatballs", "pizza"]

for meal in meals:
    print(meal)