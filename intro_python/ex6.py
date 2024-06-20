pays = ("Belgique", "France", "Luxembourg", "Pays-bas", "Allemagne")

print(pays)

choix_pays = input("Quel pays pour son index ?\n")

print(pays.index(choix_pays))

choix_index = int(input("Quel position dans le tuple ?\n"))
print(pays[choix_index])
