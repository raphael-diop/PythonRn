entier = input("Entrez un entier : ")
count = 0
#compte de nbr de mot dans data.txt
with open("Jour3/data.txt", "r") as fichier:
    data = fichier.read()
    mots = data.split()
    for mot in mots:
        if len(mot) == int(entier):
            count += 1

print("Il y a ", count, " mots contenants ", entier, " lettres.")