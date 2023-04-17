text = input("écris un texte : ")

with open("Jour3/Job0/output.txt", "w") as fichier:
    fichier.write(text)
    print("Le texte a été écrit dans le fichier output.txt")