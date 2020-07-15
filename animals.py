# import the python datetime module to help us create a timestamp
from datetime import date

# Petting area animals
class Llama:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

class Donkey:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

class Goat:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

class Alpaca:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

class Pig:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

# Glass tank animals
class Snake:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

class Lizard:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

class Tortoise:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

class Turtle:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

class Alligator:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

# Pond animals
class Fish:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Bird:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

class Frog:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

class Toad:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

class Duck:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift

barbara = Llama("Barbara", "Domestic Llama", "morning")
print(barbara.name)

kong = Donkey("Kong", "African Wild Ass", "midday")
print(kong.name)

tom_brady = Goat("Tom Brady", "Wild Goat", "afternoon")
print(tom_brady.name)

fluffy = Alpaca("Fluffy", "Domestic Alpaca", "morning")
print(fluffy.name)

porky = Pig("Porky", "Pot Belly Pig", "midday")
print(porky.name)

bertha = Snake("Bertha", "Green Anaconda")
print(bertha.name)

jose = Lizard("Jose", "Mexican Beaded Lizard", "afternoon")
print(jose.name)

wayne = Tortoise("Wayne", "Galapagos Tortoise", "morning")
print(wayne.name)

michelangelo = Turtle("Michelangelo", "Teenage Mutant Ninja Turtle", "midday")
print(michelangelo.name)

chompy = Alligator("Chompy", "American Alligator", "afternoon")
print(chompy.name)

nemo = Fish("Nemo", "Clown Fish")
print(nemo.name)

miss_blue = Bird("Miss Blue", "Great Blue Turaco", "morning")
print(miss_blue.name)

frogger = Frog("Frogger", "Green Frog", "midday")
print(frogger.name)

mr_toad = Toad("Mr. Toad", "Common Toad", "afternoon")
print(mr_toad.name)

donald = Duck("Donald", "American Pekin Duck", "morning")
print(donald.name)

print(f'{donald.name} the {donald.species} is available to pet during the {donald.shift}.')


