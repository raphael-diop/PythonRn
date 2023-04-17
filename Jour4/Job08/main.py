labyrinthe = []

#On lis le fichier et on stocke le labyrinthe dans une matrice
def lire_labyrinthe():
    with open("Jour4/maze.mz", "r") as fichier:
        for ligne in fichier:
            labyrinthe.append(list(ligne.strip()))

lire_labyrinthe()

#on defini si une case est ouverte ou non 
def is_open(x, y):
    if labyrinthe[y][x] == ".":
        return True
    else:
        return False

#on defini la case d'entrée et de sortie
entry = (0, 0)
exit = (len(labyrinthe[0]) - 1, len(labyrinthe) - 1)

#on cherche le chemin le plus rapide pour sortir du labyrinthe avec l'olgorithme A*
open_list = []
def find_path(entry, exit):
    #on defini les variables
    
    closed_list = []
    current = entry
    open_list.append(current)
    #on cherche le chemin le plus rapide
    while current != exit:
        #on cherche les cases adjacentes
        adjacent = []
        if current[0] > 0:
            adjacent.append((current[0] - 1, current[1]))
        if current[1] > 0:
            adjacent.append((current[0], current[1] - 1))
        if current[0] < len(labyrinthe[0]) - 1:
            adjacent.append((current[0] + 1, current[1]))
        if current[1] < len(labyrinthe) - 1:
            adjacent.append((current[0], current[1] + 1))
        #on cherche les cases adjacentes ouvertes
        adjacent_open = []
        for case in adjacent:
            if is_open(case[0], case[1]):
                adjacent_open.append(case)
        #on cherche les cases adjacentes non visitées
        adjacent_not_visited = []
        for case in adjacent_open:
            if case not in closed_list:
                adjacent_not_visited.append(case)
        #on cherche la case adjacente avec la plus petite distance
        min_distance = []
        for case in adjacent_not_visited:
            distance = abs(exit[0] - case[0]) + abs(exit[1] - case[1])
            min_distance.append(distance)

        for case in adjacent_not_visited:
            distance = abs(exit[0] - case[0]) + abs(exit[1] - case[1])
            if distance == min_distance:
                current = case
                open_list.append(current)
                break
        #on ajoute la case actuelle à la liste des cases visitées
        closed_list.append(current)
    #on affiche le chemin le plus rapide
    for case in open_list:
        labyrinthe[case[1]][case[0]] = "x"
    for ligne in labyrinthe:
        print("".join(ligne))

find_path(entry, exit)

with open("maze-out.mz", "w") as file:
    # Écrire le contenu modifié du labyrinthe dans le fichier
    for row in open_list:
        file.write("".join(row) + "\n")
print("Le fichier sortie trouvée")

        