class Livre():
    def __init__(self, titre: str, auteur: str, isbn: str):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn

class LivreNumerique(Livre):
    def __init__(self, titre, auteur, isbn, taille_fichier: str):
        super().__init__(titre, auteur, isbn)
        self.taille_fichier = taille_fichier

class Bibliothèque():
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def supprimer_livre(self, isbn):
        for livre in self.livres:
            if livre.isbn == isbn:
                self.livres.remove(livre)
                return True
        return False  #si pas trouvé

    def rechercher_par_titre(self, titre):
        return [livre for livre in self.livres if titre.lower() in livre.titre.lower()]

    def rechercher_par_auteur(self, auteur):
        return [livre for livre in self.livres if auteur.lower() in livre.auteur.lower()]

bibliotheque = Bibliothèque()
livre1 = Livre("harry potter", "harry", "01")
livre2 = LivreNumerique("le hobbit", "jk rowling", "02", "1GO")

bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)

print("Recherche par titre 'harry potter' :", bibliotheque.rechercher_par_titre("harry potter"))
print("Recherche par auteur 'jk rowling' :", bibliotheque.rechercher_par_auteur("jk rowling"))