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

def mot_est_trouve(mot, lettres_trouvees):
    """Retourne True si toutes les lettres du mot ont ete devinees."""
    mot_sans_accent = enlever_accents(mot)
    for lettre in mot_sans_accent:
        if lettre not in lettres_trouvees:
            return False
    return True

def demander_lettre(lettres_jouees):
    """Demande une lettre a l'utilisateur et la retourne.
    Verifie que la saisie est bien une seule lettre de l'alphabet
    et qu'elle n'a pas deja ete jouee."""
    lettre_valide = False
    lettre = ""
    while not lettre_valide:
        saisie = input("Entrez une lettre : ").lower()
        if len(saisie) != 1:
            print("Veuillez entrer une seule lettre.")
        elif not saisie.isalpha():
            print("Ce n'est pas une lettre valide.")
        elif saisie in lettres_jouees:
            print("Vous avez deja joue cette lettre.")
        else:
            lettre = saisie
            lettre_valide = True
    return lettre

def donner_indice(mot, lettres_jouees):
    """BONUS : retourne une lettre de l'alphabet qui n'est PAS dans le mot
    et qui n'a pas deja ete jouee. Retourne None si aucune lettre possible."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    mot_sans_accent = enlever_accents(mot)
    lettres_possibles = []
    for lettre in alphabet:
        if lettre not in mot_sans_accent and lettre not in lettres_jouees:
            lettres_possibles.append(lettre)
    if len(lettres_possibles) == 0:
        return None
    return random.choice(lettres_possibles)


def jouer_partie(liste_mots):
    """Joue une partie complete du pendu. Retourne True si le joueur gagne,
    False s'il perd. C'est la fonction qui contient la boucle while."""
    mot = choisir_mot(liste_mots)
    chances = CHANCES_DEPART
    lettres_trouvees = []  # lettres correctes deja devinees
    lettres_jouees = []    # toutes les lettres proposees (bonnes ou mauvaises)
 
    print("\nUn nouveau mot a ete choisi. Bonne chance !")
    print("Le mot contient", len(mot), "lettres.\n")
 
    # Boucle de jeu : on continue tant qu'il reste des chances
    while chances > 0:
        # 1. Afficher l'etat actuel du mot
        print("Mot :", afficher_etat(mot, lettres_trouvees))
        print("Chances restantes :", chances)

        # BONUS : proposer un indice s'il reste au moins une chance
        veut_indice = input("Voulez-vous un indice ? (o/n) : ")
        if veut_indice.lower() == "o":
            indice = donner_indice(mot, lettres_jouees)
            if indice is None:
                print("Aucun indice disponible.")
            else:
                print("Indice : la lettre '" + indice + "' n'est pas dans le mot.")
                lettres_jouees.append(indice)
                chances = chances - 1  # l'indice coute une chance
                # Si l'indice fait tomber les chances a zero, on arrete
                if chances == 0:
                    break
 
        # 2. Demander une lettre a l'utilisateur
        lettre = demander_lettre(lettres_jouees)
        lettres_jouees.append(lettre)
 
        # 3. Indiquer si la lettre fait partie du mot
        mot_sans_accent = enlever_accents(mot)
        if lettre in mot_sans_accent:
            print(">> Bien joue ! La lettre '" + lettre + "' est dans le mot.\n")
            lettres_trouvees.append(lettre)
        else:
            print(">> Dommage. La lettre '" + lettre + "' n'est pas dans le mot.")
            # 4. Mettre a jour les chances
            chances = chances - 1
            print("\n")
 
        # Verifier la victoire apres chaque tour
        if mot_est_trouve(mot, lettres_trouvees):
            print("Felicitations ! Vous avez trouve le mot :", mot)
            return True
 
    # Si on sort de la boucle, c'est que les chances sont epuisees
    print("Vous avez perdu. Le mot etait :", mot)
    return False

def rejouer():
    """Demande a l'utilisateur s'il veut recommencer une partie.
    Retourne True pour rejouer, False pour quitter."""
    reponse = input("\nVoulez-vous rejouer ? (o/n) : ")
    return reponse.lower() == "o"

def main():
    """Point d'entree du programme : charge les mots du fichier
    et enchaine les parties tant que le joueur veut continuer."""
    print("=== JEU DU PENDU ===\n")
 
    mots = charger_mots(FICHIER_MOTS)
 
    # Si aucun mot n'a pu etre charge, on arrete le programme
    if len(mots) == 0:
        print("Impossible de charger les mots. Verifiez le fichier",
              FICHIER_MOTS + ".")
        return
 
    continuer = True
    while continuer:
        jouer_partie(mots)
        continuer = rejouer()

 
    print("\nMerci d'avoir joue. A bientot !")

main()

