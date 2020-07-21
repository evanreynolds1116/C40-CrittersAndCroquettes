from animals import Goose, Alligator, Alpaca, Bird, Donkey, Duck, Fish, Frog, Goat, Lizard, Llama, Pig, Snake, Toad, Tortoise, Turtle
from attractions import PettingZoo, SnakePit, Wetlands

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

# Create a Goose
bob = Goose("Bob", "Canada goose", "watercress sandwiches", 12341)
bob.run()
bob.swim()

# Create an attraction
varmint_village = PettingZoo("Varmint Village", "critters that like to dig and scurry")
varmint_village.add_animal(bob)


for animal in varmint_village.animals:
    print(animal)

snake_pit = SnakePit("Snake Pit", "snakes and stuff")
snake_pit.add_animal(bertha)

for animal in snake_pit.animals:
    print(animal)

wet_lands = Wetlands("Wetlands", "wide variety of animals in here")
wet_lands.add_animal(nemo)

for animal in wet_lands.animals:
    print(animal)
