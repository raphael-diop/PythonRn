class Personne:
    def __init__(self, nom, prenom):
        self._nom = nom
        self._prenom = prenom

    def SePresenter(self):
        print("Je m'appelle", self._prenom, self._nom)

    def get_nom(self):
        return self._nom

    def set_nom(self, nom):
        self._nom = nom

    def get_prenom(self):
        return self._prenom

    def set_prenom(self, prenom):
        self._prenom = prenom



personne1 = Personne("Raph", "Raph")
personne2 = Personne("Bernard", "Bernard")
personne3 = Personne("Paul", "Paul")
personne1.set_prenom("Volodimir")
personne1.SePresenter() 
personne2.SePresenter() 
personne3.SePresenter() 
print(personne1.get_prenom())