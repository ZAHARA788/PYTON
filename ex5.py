note = float(input("entrez la note (0-20): "))
if note >= 16 :
    print("mention très bien")
else note >= 14 :
    print("mention bien")
elif note >= 12 :
    print("mention assez bien")
elif note >=10 :
    print("mention passable")
else :
    print("insuffisant")