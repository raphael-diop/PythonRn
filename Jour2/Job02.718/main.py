class Personne:
    def __init__(self, nom, prenom):
        self._nom = nom
        self._prenom = prenom

    def get_nom(self):
        return self._nom

    def set_nom(self, nom):
        self._nom = nom

    def get_prenom(self):
        return self._prenom

    def set_prenom(self, prenom):
        self._prenom = prenom


class Auteur(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.oeuvre = []

    def listerOeuvre(self):
        print("Oeuvre de", self._prenom, self._nom, ":")
        for livre in self.oeuvre:
            livre.print()

    def ecrireUnLivre(self, titre):
        livre = Livre(titre, self)
        self.oeuvre.append(livre)
        return livre


class Livre:
    def __init__(self, titre, auteur):
        self._titre = titre
        self._auteur = auteur

    def print(self):
        print(self._titre, "par", self._auteur.get_prenom(), self._auteur.get_nom())


class Client(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.collection = []

    def inventaire(self):
        print("Livres en possession de", self._prenom, self._nom, ":")
        if len(self.collection) == 0:
            print("Aucun livre")
            return
        for livre in self.collection:
            livre.print()


class Bibliotheque:
    def __init__(self, nom):
        self._nom = nom
        self.catalogue = {}

    def acheterLivre(self, auteur, titre, quantite,vendeur):
        for livre in auteur.oeuvre:
            if livre._titre == titre:
                self.catalogue[livre] = quantite
                print("ACHAT:",quantite, "exemplaire(s) de","/", livre._titre, "écris par", auteur.get_prenom(), auteur.get_nom(),"acheté(s) à", vendeur,"/")
                return
        print("Le livre", titre, "n'existe pas dans l'oeuvre de", auteur.get_prenom(), auteur.get_nom())

    def inventaire(self):
        print("Catalogue de la bibliothèque", self._nom, ":")
        for livre, quantite in self.catalogue.items():
            print("INVENAIRE:",livre._titre, "par", livre._auteur.get_prenom(), livre._auteur.get_nom(), "x", quantite)

    def louer(self, client, titre):
        for livre, quantite in self.catalogue.items():
            if livre._titre == titre and quantite > 0:
                client.collection.append(livre)
                # if quantite >= 2:
                #     self.catalogue[livre] -= 1
                #     quantite + 1
                #     print("LOCATION:",client.get_prenom(), client.get_nom(), "a loué", livre._titre, "à", self._nom, "x", quantite)
                #     return
                self.catalogue[livre] -= 1
                print("LOCATION:",client.get_prenom(), client.get_nom(), "a loué", livre._titre, "à", self._nom)
                return
        print("Le livre", titre, "n'est pas disponible dans la bibliothèque:", self._nom)

    def rendreLivres(self, client):
        for livre in client.collection:
            if livre in self.catalogue:
                self.catalogue[livre] += 1
            else:
                self.catalogue[livre] = 1
        client.collection = []
        print("RETOUR:",client.get_prenom(), client.get_nom(),"à rendu", livre._titre, "à", self._nom)

auteur1 = Auteur("Hugo", "Victor")
auteur2 = Auteur("Shakespeare", "William")

livre1 = auteur1.ecrireUnLivre("Les Misérables")
livre2 = auteur1.ecrireUnLivre("Notre-Dame de Paris")
livre3 = auteur2.ecrireUnLivre("Hamlet")
livre4 = auteur2.ecrireUnLivre("Macbeth")

biblio1 = Bibliotheque("Bibliothèque du Beau Bouquin")
biblio1.acheterLivre(auteur1, "Les Misérables", 5,"Amazon")
biblio1.acheterLivre(auteur1, "Notre-Dame de Paris", 3,"Libraire de France")
biblio1.acheterLivre(auteur2, "Macbeth", 2,"Pariculier")
biblio1.inventaire()

client1 = Client("Dupont", "Pierre")
client2 = Client("Martin", "Sophie")

biblio1.louer(client1, "Les Misérables")
biblio1.louer(client1, "Les Misérables")
biblio1.louer(client2, "Macbeth")
client1.inventaire()
client2.inventaire()

biblio1.rendreLivres(client2)
client2.inventaire()
client1.inventaire()
biblio1.inventaire()

