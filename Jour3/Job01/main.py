countDom = 0
countMots = 0
#compte de domains.xml
with open("Jour3/Job01/domains.xml", "r") as fichier:
    for line in fichier:
        if '<column name="domain">' in line:
            countDom += 1
print("Nombre de domaines:",countDom)


#compte de nbr de mot dans data.txt
with open("Jour3/data.txt", "r") as fichier:
    data = fichier.read()
    mots = len(data.split())

print("Nombre de mots:",mots)
