# Test technique — Trustia

Ce repository contient :
- **Exercice 1** : affichage de blocs de texte encadrés en console (Python)
- **Exercice 2** : application web Django (produits + factures)

## Stack

- **Python**
- **Django** (Exercice 2)
- **HTML / CSS / JavaScript** (templates Django)
- **SQLite** (base de données par défaut)
- **Docker / Docker Compose** (optionnel, pour lancer l’Exercice 2 facilement)

## Exercice 1 — Blocs de texte encadrés

### Objectif
Afficher dans la console des **blocs de texte encadrés** (ASCII) comme dans l’exemple fourni.

### Lancer le programme

```bash
python3 exo1.py
```

### Contraintes respectées
- **Largeur maximale**: configurable via `MAX_WIDTH` (valeur utilisée: 100).
- **Tout en minuscules**: les phrases sont affichées avec `.lower()`.
- **Blocs multi-lignes**: chaque bloc peut contenir 1 ou plusieurs lignes.
- **Bordures**: `-` pour les lignes haut/bas, `|` pour les côtés.

### Organisation des données
- **Phrases**: stockées dans le dictionnaire `phrases`.
- **Certaines phrases peuvent rester sans être affichées**: via les règles d’exclusion.
- **Ordre des blocs modifiable facilement**: via la liste `ordre_blocs`.
- **Composition des blocs**: via le dictionnaire `blocs` (liste de clés de phrases par bloc).
- **Exclusions**: certaines phrases sont masquées selon le bloc via `exclusions_par_bloc`.

## Exercice 2 — Django (Produits & Factures)

La doc et les scénarios de test sont dans [`exo2/README.md`](exo2/README.md) et [`TESTING.md`](TESTING.md).

### Démarrer rapidement (Docker)

```bash
cd exo2
docker compose up --build
```

Puis ouvrir `http://127.0.0.1:8000/`.

### Démarrer en local (venv)

Depuis la racine du repo :

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

cd exo2
python manage.py migrate
python manage.py runserver
```