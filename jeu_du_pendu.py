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
        with open(fichier, "r", encoding="utf-8") as fichier:
            for ligne in fichier:
                mot = ligne.strip()  # enleve les espaces et le retour a la ligne
                if mot != "":         # on ignore les lignes vides
                    liste_de_mots.append(mot)
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

def afficher_etat(mot, lettres_trouvees):
    """Construit et retourne l'etat actuel du mot : les lettres devinees
    sont affichees, les autres sont remplacees par un _.
    La comparaison se fait sur la version sans accent du mot."""
    mot_sans_accent = enlever_accents(mot)
    affichage = ""
    for position in range(len(mot)):
        lettre = mot_sans_accent[position]
        if lettre in lettres_trouvees:
            # On affiche la vraie lettre (avec accent eventuel)
            affichage = affichage + mot[position] + " "
        else:
            affichage = affichage + "_ "
    return affichage

def main(liste_mots):
    """Point d'entree du programme : charge les mots du fichier
    et enchaine les parties tant que le joueur veut continuer."""
    lettres_trouvees = []
    print("=== JEU DU PENDU ===\n")
 
    mots = charger_mots(FICHIER_MOTS)
    mot = choisir_mot(liste_mots)

 
    # Si aucun mot n'a pu etre charge, on arrete le programme
    if len(mots) == 0:
        print("Impossible de charger les mots. Verifiez le fichier",
              FICHIER_MOTS + ".")
        return
 
    continuer = True

    afficher_etat(mot, lettres_trouvees)
    
    print("\nMerci d'avoir joue. A bientot !")


main()

