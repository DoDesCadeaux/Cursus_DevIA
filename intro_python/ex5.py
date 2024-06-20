#1
animaux = ["lapin", "chat", "chien", "chiot", "dragon", "ornithorynque"]

def ex1(animaux: list):
    print(animaux)

def ex2(animaux: list):
    for i in animaux:
        print(i)
        print(f"Len de {i} = {len(i)}")

def ex3():
    chiffres = [86, 12, 343, 1, 4343, 232, -213, 342, 1123, 433, 2]
    mini = 2^31
    for i in chiffres:
        if i < mini:
            mini = i
    return mini


def ex4():
    even = [x for x in range(1, 21) if x % 2 == 0]
    print(even)

if __name__ == '__main__':
    #ex1(animaux)
    #ex2(animaux)
    #print(ex3())
    ex4()
