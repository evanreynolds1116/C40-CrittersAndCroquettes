# import the python datetime module to help us create a timestamp
from datetime import date

class Animal:
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.food = food
        self.__chip_num = chip_num
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    @property # the getter
    def chip_num(self):
        return self.__chip_num

    @chip_num.setter # the setter
    def chip_num(self, number):
        pass

# Petting area animals
class Llama(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")} while having their tummy rubbed')

class Donkey(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        (f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")} while having their ears scratched')

class Goat(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        (f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")} while watching Tom Brady hype videos')

class Alpaca(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Pig(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"

# Glass tank animals
class Snake(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Lizard(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Tortoise(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Turtle(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Alligator(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"

# Pond animals
class Fish(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Bird(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Frog(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Toad(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Duck(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"

barbara = Llama("Barbara", "Domestic Llama", "morning", "Llama Chow", 12345)

kong = Donkey("Kong", "African Wild Ass", "midday", "Donkey Chow", 12346)

tom_brady = Goat("Tom Brady", "Wild Goat", "afternoon", "Goat Chow", 12347)

fluffy = Alpaca("Fluffy", "Domestic Alpaca", "morning", "Alpaca Chow", 12348)

porky = Pig("Porky", "Pot Belly Pig", "midday", "Pig Chow", 12349)

bertha = Snake("Bertha", "Green Anaconda", "Snake Chow", 23456)

jose = Lizard("Jose", "Mexican Beaded Lizard", "afternoon", "Lizard Chow", 23457)

wayne = Tortoise("Wayne", "Galapagos Tortoise", "morning", "Tortoise Chow", 23458)

michelangelo = Turtle("Michelangelo", "Teenage Mutant Ninja Turtle", "midday", "Turtle Chow", 23459)

chompy = Alligator("Chompy", "American Alligator", "afternoon", "Alligator Chow", 34567)

nemo = Fish("Nemo", "Clown Fish", "Fish Chow", 34568)

miss_blue = Bird("Miss Blue", "Great Blue Turaco", "morning", "Bird Chow", 34569)

frogger = Frog("Frogger", "Green Frog", "midday", "Frog Chow", 45678)

mr_toad = Toad("Mr. Toad", "Common Toad", "afternoon", "Toad Chow", 45679)

donald = Duck("Donald", "American Pekin Duck", "morning", "Duck Chow", 56789)



    
