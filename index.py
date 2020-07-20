from animals import barbara, kong, tom_brady, fluffy, porky, bertha, jose, wayne, michelangelo, chompy, nemo, miss_blue, frogger, mr_toad, donald

from attractions import PettingZoo, SnakePit, Wetlands

pet_palace = PettingZoo("Pet Palace", "animals that are safe to pet")
snake_station = SnakePit("Snake Station", "things that scare me")
wet_works = Wetlands("Wet Works", "many different animals")

pet_palace.add_animal([barbara, kong, tom_brady, fluffy, porky])

snake_station.add_animal([bertha, jose, wayne, michelangelo, chompy])

wet_works.add_animal([nemo, miss_blue, frogger, mr_toad, donald])

print(f"{pet_palace.attraction_name} is where you'll find {pet_palace.description}, like:")
for animal in pet_palace.animals:
    print(f"* {animal.name} the {animal.species}")

print(f"{snake_station.attraction_name} is where you'll find {snake_station.description}, like:")
for animal in snake_station.animals:
    print(f"* {animal.name} the {animal.species}")

print(f"{wet_works.attraction_name} is where you'll find {wet_works.description}, like:")
for animal in wet_works.animals:
    print(f"* {animal.name} the {animal.species}")

print(pet_palace.last_critter_added)
print(snake_station.last_critter_added)
print(wet_works.last_critter_added)



