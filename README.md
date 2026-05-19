# Jeu du Pendu

Mini-projet du cours MGA802 (Introduction a la programmation avec Python).

C'est un jeu du pendu qui se joue dans le terminal. Le programme tire un mot
au hasard et on doit le deviner lettre par lettre. On a droit a 6 erreurs.

## Les fichiers

- `pendu.py` : le jeu. Tout est ecrit sous forme de fonctions, comme demande
  dans la consigne.
- `mots_pendu.txt` : la liste des mots, un par ligne. C'est dans ce fichier
  que le programme va piocher.
- `.gitignore` : pour ne pas envoyer le dossier `.idea` de PyCharm sur le repo.

## Pour jouer

Il faut Python 3. On garde `pendu.py` et `mots_pendu.txt` dans le meme
dossier, puis on lance dans un terminal :

```
python pendu.py
```

Ensuite il suffit de suivre ce qui s'affiche. A chaque tour le jeu montre le
mot avec des `_` pour les lettres pas encore trouvees, demande une lettre, et
dit si elle est dans le mot ou pas. Quand on trouve le mot ou qu'on n'a plus
de chances, il propose de rejouer ou de quitter.

## Quelques details

Si on veut jouer avec ses propres mots, il suffit de remplacer le contenu de
`mots_pendu.txt`. Le nom du fichier ne change pas, juste les mots dedans.

Les accents sont geres : taper `e` marche aussi pour un `e` accentue, pareil
pour les autres voyelles. Pas besoin de chercher comment taper un accent.

Il y a aussi un bonus : a chaque tour on peut demander un indice, et le jeu
revele alors une lettre qui n'est pas dans le mot. Par contre ca coute une
chance, donc a utiliser quand on est vraiment bloque.