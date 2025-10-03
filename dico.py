# données de départ
etudiants = [
    {"nom": "Alice", "note": 15, "annee": 2},
    {"nom": "Bob", "note": 12, "annee": 1},
    {"nom": "Charlie", "note": 18, "annee": 2}
]

# exo 1. filtrer les étudiants admis (note >= 12)
admis = [e for e in etudiants if e["note"] >= 12]
print("Étudiants admis :", admis)

# exo 2. calculer la moyenne par année
from collections import defaultdict

notes_par_annee = defaultdict(list)
for e in etudiants:
    notes_par_annee[e["annee"]].append(e["note"])

moyenne_par_annee = {annee: sum(notes)/len(notes) for annee, notes in notes_par_annee.items()}
print("Moyenne par année :", moyenne_par_annee)

# exo 3. créer un dictionnaire nom -> mention
def get_mention(note):
    if note >= 16:
        return "Très bien"
    elif note >= 14:
        return "Bien"
    elif note >= 12:
        return "Assez bien"
    else:
        return "Ajourné"

mentions = {e["nom"]: get_mention(e["note"]) for e in etudiants}
print("Dictionnaire nom → mention :", mentions)
