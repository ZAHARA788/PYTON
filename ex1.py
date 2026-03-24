montant = int(input("Quel est le montant : "))
pourcentage = int (input("quel est le pourcentage : "))
pourcentage = montant *pourcentage / 100
print(f"pourboire : {pourcentage}$.")
total= pourcentage + montant
print (f"total : {total}$.")

