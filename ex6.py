temperature = int(input("entrez la temperature : "))
if temperature < 0 :
    print("gel")
elif temperature > 0 and temperature < 15 :
    print("froid")
elif  temperature > 15 and temperature < 25 :
    print("agreable")
else :
     print ("choud")
