## Animal is-a object (yes, sort of confusing) look at the eaxtra credit
class Animal(object):
    pass

## Dog is-a Animal
## class Dog has-a __init__ that takes self and name params
class Dog(Animal):

    def __init__(self, name):
        ## from self, get the name attribute and set it to name
        ## Dog has-a name
        self.name = name.lower()

    def turn_around(self):
        str = ""
        for letter in self.name:
            str = letter + str
        print(f"{self.name}'s name backwards is {str.capitalize()}.")

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

    def meow(self):
        print(f"{self.name} is meowing.")

    def meals(self):
        menu = {
            "Monday": "tuna",
            "Tuesday": "crackers",
            "Wednesday": "applesauce",
            "Thursday": "spaghetti",
            "Friday": "pizza"
        }
        for day, food in menu.items():
            print(f"On {day}, {self.name} ate {food}.")

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

    def walk_pet(self):
        print(f"{self.name} walked their pet {self.pet} around the block.")

## Employee is a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        ## https://docs.python.org/3/library/functions.html#super
        ## https://rhettinger.wordpress.com/2011/05/26/super-considered-super/
        ## It seems like it's calling the "parent" class?
        ## same as:
        ## def __init__(self, name):
        ##    super().__init__(name)
        super(Employee, self).__init__(name)
        ## Employee (and person?) has-a salary
        self.salary = salary


## Fish is-a object
class Fish(object):
    pass

## Salmon is a Fish
class Salmon(Fish):
    pass

## Halibut is a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")
rover.turn_around()

## satan is-a Cat
satan = Cat("Satan")
satan.meow()
angel = Cat("Angel")
angel.meals()
## mary is-a person
mary = Person("Mary")
print(f"Mary's name is {mary.name}")

## mary has a pet
mary.pet = satan.name
print(f"{mary.name} has a pet cat named {mary.pet}.")
mary.walk_pet()

## frank is an employee
frank = Employee("Frank", 120000)
frank.pet = rover.name
frank.walk_pet()
print(f"{frank.name}'s salary is {frank.salary}.")

## frank has-a pet
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()