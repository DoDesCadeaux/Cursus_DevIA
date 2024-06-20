plats = {}
for i in range(1, 5):
    plat = input(f"Entrez votre plat préféré numéro {i} : ")
    plats[i] = plat

print("Voici vos plats préférés :", plats)

plat_moins_aime = input("Quel est le plat que vous aimez le moins ? ")

cle_a_suppr = None
for cle, valeur in plats.items():
    if valeur == plat_moins_aime:
        cle_a_suppr = cle
        break

if cle_a_suppr is not None:
    del plats[cle_a_suppr]
else:
    print("Le plat n'est pas dans la liste.")

print("Voici votre nouveau dictionnaire des plats :", plats)

plats_tries = dict(sorted(plats.items(), key=lambda item: item[1]))
print("Voici votre dictionnaire des plats préférés trié :", plats_tries)

