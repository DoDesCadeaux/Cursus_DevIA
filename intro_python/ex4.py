#1
def ex1():
    prenom = input("Prenom ?\n")
    combien = int(input("Combien de fois l'afficher ?\n"))

    for _ in range(0, combien):
        print(prenom)

#2
def ex2():
    mult = int(input("Quelle table ?\n"))
    for i in range(1, 10):
        print(i * mult)


if __name__ == '__main__':
    #ex1()
    ex2()
