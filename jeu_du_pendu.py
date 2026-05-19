import random
import math 

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

