class PettingZoo:
    
    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animals):
        self.animals.extend(animals)

class SnakePit:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animals):
        self.animals.extend(animals)

class Wetlands:
    
    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animals):
        self.animals.extend(animals)