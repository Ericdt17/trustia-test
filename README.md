# Exercice 1— Blocs de texte encadrés

## Objectif
Afficher dans la console des **blocs de texte encadrés** (ASCII) comme dans l’exemple fourni.

## Lancer le programme

```bash
python3 exo1.py
```

## Contraintes respectées
- **Largeur maximale**: configurable via `MAX_WIDTH` (valeur utilisée: 100).
- **Tout en minuscules**: les phrases sont affichées avec `.lower()`.
- **Blocs multi-lignes**: chaque bloc peut contenir 1 ou plusieurs lignes.
- **Bordures**: `-` pour les lignes haut/bas, `|` pour les côtés.

## Organisation des données
- **Phrases**: stockées dans le dictionnaire `phrases`.
- **Certaines phrases peuvent rester sans être affichées**: via les règles d’exclusion.
- **Ordre des blocs modifiable facilement**: via la liste `ordre_blocs`.
- **Composition des blocs**: via le dictionnaire `blocs` (liste de clés de phrases par bloc).
- **Exclusions**: certaines phrases sont masquées selon le bloc via `exclusions_par_bloc`.