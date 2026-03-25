mot = input("entrez le nom : ")
compteur=0
for letre in mot: 
    if letre in ("a"):
        compteur = compteur + 1
        print(f"le mot '{mot}' contient {compteur} a")