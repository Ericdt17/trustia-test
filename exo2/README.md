# Exercice 2 — Django (Produits & Factures)

## Lancer le projet

### Option A — en local (venv)

Depuis la racine du repo :

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

cd exo2
python manage.py migrate
python manage.py runserver
```

Puis ouvrir `http://127.0.0.1:8000/`.

### Option B — avec Docker (recommandé pour le recruteur)

Depuis le dossier `exo2/` :

```bash
docker compose up --build
```

Puis ouvrir `http://127.0.0.1:8000/`.

Au démarrage, le conteneur :
- applique automatiquement les migrations
- injecte **50 produits** si la base est vide (commande `seed_products`)

## Produits (CRUD + pagination)

| URL | Action |
|-----|--------|
| `/` | Liste des produits (pagination : **10** par page) |
| `/products/new/` | Créer un produit |
| `/products/<id>/edit/` | Modifier un produit |
| `/products/<id>/delete/` | Supprimer un produit (confirmation) |

Champs : **nom**, **prix** (strictement positif), **date de péremption**.

## Factures (création + lignes + liste paginée)

| URL | Action |
|-----|--------|
| `/invoices/` | Liste des factures (pagination : **10** par page) |
| `/invoices/new/` | Créer une facture : plusieurs lignes **produit + quantité** |
| `/invoices/<id>/` | Détail : lignes (produit, prix unitaire, quantité) |

Règles : au moins une ligne ; pas deux fois le même produit sur une même facture.

La page détail facture affiche aussi :
- le **nombre total de produits** (somme des quantités)
- le **total à payer** (somme `prix × quantité`)

## Modèles (base de données)

- `Product`: `name`, `price`, `expiry_date`
- `Invoice`
- `InvoiceItem`: lien Facture ↔ Produit + `quantity`

## Données de démo

- Injecter 50 produits (local) :

```bash
python manage.py seed_products --count 50
```
