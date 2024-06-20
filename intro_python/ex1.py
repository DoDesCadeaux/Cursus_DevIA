#1

texte: str = "Le texte"
entier: int = 78
pi: float = 3.1415

print(f"Types: {type(texte)}, {type(entier)}, {type(pi)}")


#2
a = 3
result = (a == 3)
print(type(a))
print(type(result))

#3
text = "Bonjour, monde!"
print(f"{text[::-1]}")

#4
gt_hund = int(input("Entrez un nbr > 100\n"))
lt_ten = int(input("Entrew un nb < 10\n"))

if (gt_hund <= 100) or not isinstance(gt_hund, int):
    print("Erreur. Nbre doit etre plus grand que 100")
    exit(1)
elif (lt_ten >= 10) or not isinstance(lt_ten, int):
    print("Erreur. Nbre doit etre plus petit que 10")
    exit(1)

print(f"{lt_ten} entre {gt_hund // lt_ten} fois dans {gt_hund}")

#5
r = int(input("Entrez un rayon\n"))
v = (4/3) * 3.14 * (r)**3

print(f"Volume = {v:.2f}")
