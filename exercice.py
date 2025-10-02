import json
import csv
import os

class Livre:
    def __init__(self, titre: str, auteur: str, isbn: str):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn

    def to_dict(self):
        return {
            "type": "Livre",
            "titre": self.titre,
            "auteur": self.auteur,
            "isbn": self.isbn
        }

    @staticmethod
    def from_dict(data: dict):
        return Livre(data["titre"], data["auteur"], data["isbn"])

class LivreNumerique(Livre):
    def __init__(self, titre: str, auteur: str, isbn: str, taille_fichier: str):
        super().__init__(titre, auteur, isbn)
        self.taille_fichier = taille_fichier

    def to_dict(self):
        base = super().to_dict()
        base["type"] = "LivreNumerique"
        base["taille_fichier"] = self.taille_fichier
        return base

    @staticmethod
    def from_dict(data: dict):
        return LivreNumerique(data["titre"], data["auteur"], data["isbn"], data["taille_fichier"])

class Bibliotheque:
    def __init__(self):
        self.catalogue = []

    def ajouter_livre(self, livre: Livre):
        self.catalogue.append(livre)

    def afficher_catalogue(self):
        for livre in self.catalogue:
            print(f"- {livre.titre} ({livre.auteur}), ISBN: {livre.isbn}")

    #sauvegarde JSON
    def sauvegarder_json(self, chemin: str):
        try:
            data = [livre.to_dict() for livre in self.catalogue]
            with open(chemin, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"données sauvegardées dans {chemin}")
        except PermissionError:
            print("erreur : permissions insuffisantes pour écrire le fichier.")
        except Exception as e:
            print(f"erreur inattendue lors de la sauvegarde JSON : {e}")

    #chargement JSON
    def charger_json(self, chemin: str):
        if not os.path.exists(chemin):
            print("fichier JSON inexistant, catalogue vide.")
            return
        try:
            with open(chemin, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.catalogue = []
                for item in data:
                    if item["type"] == "Livre":
                        self.catalogue.append(Livre.from_dict(item))
                    elif item["type"] == "LivreNumerique":
                        self.catalogue.append(LivreNumerique.from_dict(item))
            print(f"données chargées depuis {chemin}")
        except json.JSONDecodeError:
            print("erreur : fichier JSON invalide.")
        except Exception as e:
            print(f"erreur inattendue lors du chargement JSON : {e}")

    #export CSV
    def exporter_csv(self, chemin: str):
        try:
            with open(chemin, "w", newline="", encoding="utf-8-sig") as f:
                writer = csv.writer(f)
                writer.writerow(["titre", "auteur", "isbn", "taille_fichier"])
                for livre in self.catalogue:
                    if isinstance(livre, LivreNumerique):
                        writer.writerow([livre.titre, livre.auteur, livre.isbn, livre.taille_fichier])
                    else:
                        writer.writerow([livre.titre, livre.auteur, livre.isbn, ""])
            print(f"catalogue exporté en CSV : {chemin}")
        except PermissionError:
            print("erreur : permissions insuffisantes pour écrire le fichier CSV.")
        except Exception as e:
            print(f"erreur inattendue lors de l'export CSV : {e}")


# -------------------------------------------------------------------------
#exemple test
# ----------------------------------------------------------------------
if __name__ == "__main__":
    biblio = Bibliotheque()

    # Ajouter des livres
    biblio.ajouter_livre(Livre("1984", "George Orwell", "123456789"))
    biblio.ajouter_livre(LivreNumerique("Python 101", "Guido van Rossum", "987654321", "5Mo"))

    print("catalogue actuel :")
    biblio.afficher_catalogue()

    biblio.sauvegarder_json("catalogue.json")

    biblio.charger_json("catalogue.json")

    biblio.exporter_csv("catalogue.csv")
