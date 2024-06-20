#1
def ex1():
    while True:
        value = int(input("Choisir un nbre\n"))
        if 8 <= value <= 10:
            print(f"Value: {value}")
            return

#2
def ex2():
    previous_value = int(input("Choisir un nbre"))
    if (previous_value >= 25):
        print(f"Result: {previous_value}")
        return
    while True:
        new_value = int(input("Choisir un nbre suivant"))
        if (previous_value + new_value) >= 25:
            print(f"Result: {previous_value + new_value}")
            return
        else:
            previous_value += new_value
            continue

#3
import random
def ex3():
    essai = 0
    correct = random.randint(1, 101)
    while True:
        reponse = int(input("Un chiffre entre 1 et 100 inclus:\n"))
        essai += 1
        if (reponse > correct):
            print("C'est moins")
            continue
        elif (reponse < correct):
            print("C'est plus")
            continue
        else:
            print(f"Correct! Tu as trouve la reponse en {essai} essais")
            return

if __name__ == '__main__':
    #ex1()
    #ex2()
    ex3()

