# import the python datetime module to help us create a timestamp
from datetime import date

# Petting area animals
class Llama:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Donkey:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Goat:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Alpaca:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Pig:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

# Glass tank animals
class Snake:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

class Lizard:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Tortoise:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Turtle:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Alligator:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

# Pond animals
class Fish:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

class Bird:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Frog:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Toad:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

class Duck:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

barbara = Llama("Barbara", "Domestic Llama")
print(barbara.name)

kong = Donkey("Kong", "African Wild Ass")
print(kong.name)

tom_brady = Goat("Tom Brady", "Wild Goat")
print(tom_brady.name)

fluffy = Alpaca("Fluffy", "Domestic Alpaca")
print(fluffy.name)

porky = Pig("Porky", "Pot Belly Pig")
print(porky.name)

bertha = Snake("Bertha", "Green Anaconda")
print(bertha.name)

jose = Lizard("Jose", "Mexican Beaded Lizard")
print(jose.name)

wayne = Tortoise("Wayne", "Galapagos Tortoise")
print(wayne.name)

michelangelo = Turtle("Michelangelo", "Teenage Mutant Ninja Turtle")
print(michelangelo.name)

chompy = Alligator("Chompy", "American Alligator")
print(chompy.name)

nemo = Fish("Nemo", "Clown Fish")
print(nemo.name)

miss_blue = Bird("Miss Blue", "Great Blue Turaco")
print(miss_blue.name)

frogger = Frog("Frogger", "Green Frog")
print(frogger.name)

mr_toad = Toad("Mr. Toad", "Common Toad")
print(mr_toad.name)

donald = Duck("Donald", "American Pekin Duck")
print(donald.name)




