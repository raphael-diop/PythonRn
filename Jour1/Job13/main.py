nombres = []

#"5 saisis de nombres entiers"
for i in range(5):
    nombre = int(input("Entrez un nombre entier : "))
    nombres.append(nombre)
#organisation par ordre croissant
nombres.sort()
#affichage
print("Voici les nombres triés par ordre croissant : ")
for nombre in nombres:
    print(nombre)
