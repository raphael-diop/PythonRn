taille = int(input("Saisir un entier (taille du tableau): "))

def placer_dames(colonne, dames):
    if colonne == taille:
        return dames
    for ligne in range(taille):
        if est_valide(colonne, ligne, dames):
            resultat = placer_dames(colonne + 1, dames + [ligne])
            if resultat:
                return resultat
    return None

def est_valide(colonne, ligne, dames):
    for i in range(colonne):
        if dames[i] == ligne or \
           dames[i] - i == ligne - colonne or \
           dames[i] + i == ligne + colonne:
            return False
    return True

dames = placer_dames(0, [])
if dames:
    for i in range(taille):
        for j in range(taille):
            if dames[j] == i:
                print(" ","X", end="")
            else:
                print(" ","O", end="")
        print()
else:
    print("Aucune solution possible.")
