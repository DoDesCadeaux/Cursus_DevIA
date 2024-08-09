import random
from datetime import date

class Animal:
    def __init__(self, name, weight, height, sex, age, arrival_date):
        self.name = name
        self.weight = weight
        self.height = height
        self.sex = sex
        self.age = age
        self.arrival_date = arrival_date

    def cry(self):
        return "Cri d'animal"

    def probability_of_death(self):
        return 0

class Cat(Animal):
    def __init__(self, name, weight, height, sex, age, arrival_date, character, claws_trimmed, long_hair):
        super().__init__(name, weight, height, sex, age, arrival_date)
        self.character = character
        self.claws_trimmed = claws_trimmed
        self.long_hair = long_hair

    def probability_of_death(self):
        return 0.005

class Dog(Animal):
    def __init__(self, name, weight, height, sex, age, arrival_date, collar_color, trained, breed):
        super().__init__(name, weight, height, sex, age, arrival_date)
        self.collar_color = collar_color
        self.trained = trained
        self.breed = breed

    def probability_of_death(self):
        return 0.01

class Bird(Animal):
    def __init__(self, name, weight, height, sex, age, arrival_date, color, cage_type):
        super().__init__(name, weight, height, sex, age, arrival_date)
        self.color = color
        self.cage_type = cage_type

    def probability_of_death(self):
        return 0.03

class AnimalShelter:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def list_animals(self):
        for animal in self.animals:
            print(vars(animal))

    def count_animals(self):
        counts = {"cats": 0, "dogs": 0, "birds": 0}
        for animal in self.animals:
            if isinstance(animal, Cat):
                counts["cats"] += 1
            elif isinstance(animal, Dog):
                counts["dogs"] += 1
            elif isinstance(animal, Bird):
                counts["birds"] += 1
        return counts

    def check_deaths_overnight(self):
        deaths = []
        for animal in self.animals:
            if random.random() < animal.probability_of_death():
                deaths.append(animal)
        return deaths

shelter = AnimalShelter()

shelter.add_animal(Cat("Whiskers", 4, 25, "F", 2, date.today(), "energetic", True, True))
shelter.add_animal(Dog("Rex", 20, 50, "M", 3, date.today(), "red", True, "Labrador"))
shelter.add_animal(Bird("Tweety", 0.5, 15, "F", 1, date.today(), "yellow", "cage"))

shelter.list_animals()

counts = shelter.count_animals()
print(f"Number of cats: {counts['cats']}")
print(f"Number of dogs: {counts['dogs']}")
print(f"Number of birds: {counts['birds']}")

deaths = shelter.check_deaths_overnight()
print("Animals that died overnight:")
for animal in deaths:
    print(vars(animal))
