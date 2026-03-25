mot = input("entrez le mot : ")
compteur = 0
for mot in  ("secret123") :
    if mot in ("secret123") :
        print ("bonne")
    else :
        print ("mauvaises")
        compteur = compteur +1
        print (f"le mot '{mot}' contient {compteur}")
