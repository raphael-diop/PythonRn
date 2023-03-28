class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

class Livre:
    def __init__(self, titre, auteur, date, editeur):
        self.titre = titre
        self.auteur = auteur
        self.date   = date
        self.editeur = editeur
    
    def print(self):
        print("Titre : ", self.titre,"-", self.date,"-", self.editeur)

class Auteur(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.oeuvre = []
    
    def listerOeuvre(self):
        print("Oeuvre de ", self.prenom, self.nom)
        for livre in self.oeuvre:
            livre.print()

    def A_ecris(self, titre, date,editeur):
        livre = Livre(titre, self, date, editeur)
        self.oeuvre.append(livre)
        return livre
    

auteur1 = Auteur("Alain", "Damasio")
livre1 = auteur1.A_ecris("La Horde du Contrevent","2004","La Volte")
livre2 = auteur1.A_ecris("La Volte","2007","La Volte")
auteur2 = Auteur("George", "Tolkien")
livre1 = auteur2.A_ecris("Le Seigneur des Anneaux","1954","Hachette")
livre2 = auteur2.A_ecris("Le Hobbit","1937","Hachette")
livre3 = auteur2.A_ecris("Le Silmarillion","1977","Hachette")
auteur1.listerOeuvre()  
auteur2.listerOeuvre()  