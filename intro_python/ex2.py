#1
try:
    entier_a = int(input("Entrez un nb:\n"))
    entier_b = int(input("Entrez un second nb:\n"))
    if (entier_a > entier_b):
        print(entier_a)
    elif entier_a < entier_b:
        print(entier_b)
    else:
        print("Egaux")
except (ValueError, TypeError, KeyboardInterrupt) as e:
    print(e)
    exit(1)

#2
euro = int(input("Euros a convertir:\n"))
print(f"{euro} euros = {euro * 1.07:.2f}$")


#3
shape =  input("Triangle (T) ou Cercle (C):\n").lower()

if shape == "t":
    base = int(input("Base:\n"))
    hauteur = int(input("Hauteur:\n"))
    result = (base * hauteur) / 2
    print(f"Aire du Triangle: {result}")
elif shape == "c":
    pi = 3.14
    rayon = int(input("Rayon:\n"))
    result = pi * (rayon)**2
    print(f"Aire du cercle: {result}")
else:
    print("Erreur, doit etre C ou T")
    exit(1)
