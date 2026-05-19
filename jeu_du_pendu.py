import random

# Nombre de chances de l'utilisateur au depart
CHANCES_DEPART = 6

FICHIER_MOTS = "mots_pendu.txt"

def charger_mots(fichier):
    """ Cette fonction permet de charger le fichier texte contenant 
    les differents mots, le fichier est modifiable en gardant en tete
    qu'il faut un mot par ligne. Si le fichier n'existe pas on 
    retourne une liste vide"""

    liste_de_mots = []
    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            for ligne in fichier:
                mot = ligne.strip()  # enleve les espaces et le retour a la ligne
                if mot != "":         # on ignore les lignes vides
                    liste_mots.append(mot)
    except FileNotFoundError:
        # Le fichier n'a pas ete trouve : on retourne une liste vide
        return []
    return liste_de_mots

def enlever_accents(mot):
    """Retourne le mot en remplacant chaque lettre accentuee par sa version
    sans accent (e e e a a u ...). Permet de comparer les lettres sans
    se soucier des accents"""
    # Dictionnaire de correspondance accent -> lettre simple
    accents = {
        "a": "aaaa", "e": "eeee", "i": "iiii",
        "o": "oooo", "u": "uuuu", "c": "c",
    }
    # On reconstruit le mot lettre par lettre
    resultat = ""
    for lettre in mot:
        lettre_minuscule = lettre.lower()
        lettre_trouvee = lettre_minuscule  # par defaut, on garde la lettre
        # On cherche si la lettre fait partie d'un groupe accentue
        for lettre_simple in accents:
            if lettre_minuscule in accents[lettre_simple]:
                lettre_trouvee = lettre_simple
        resultat = resultat + lettre_trouvee
    return resultat

def choisir_mot(liste_mots):
    """Choisit et retourne un mot au hasard dans la liste fournie."""
    return random.choice(liste_mots)



