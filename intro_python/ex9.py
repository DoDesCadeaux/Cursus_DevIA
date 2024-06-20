try:
    annee = int(input("Quel est votre annee de naissance ?\n"))
    if annee < 0:
        raise Exception
    print(f"{2024 - annee}")
except ValueError:
    print("Erreur: Age doit etre un nombre")
except KeyboardInterrupt:
    print("Bonne journee")
except Exception:
   print("Quel est le secret ?") 

