from .animal import Animal
from movements import Walking, Swimming

class Donkey(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        (f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")} while having their ears scratched')