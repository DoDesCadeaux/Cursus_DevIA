class Chat:
    def __init__(self, nom, age, race):
        if not isinstance(nom, str) or not isinstance(age, int) or not isinstance(race, str):
            raise TypeError
        self.nom = nom.capitalize()
        self.age = age
        self.race = race

    def manger(self, nourriture: str):
        print(f"{self.nom} mange un peu de {nourriture} avec appetit. Miam!")

    def boire(self):
        print(f"{self.nom} boit de l'eau")

    def marcher(self, destination: str):
        print(f"{self.nom} marche vers {destination}")


try:
    chaton = Chat(nom="Rory", age=1, race="Calico")

    chaton.manger("croquettes")
    chaton.boire()
    chaton.marcher("la cuisine")

except TypeError:
    print("Mauvais type de paramatres")
