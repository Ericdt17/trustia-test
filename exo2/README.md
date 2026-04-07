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

### Option B — avec Docker

Depuis le dossier `exo2/` :

```bash
docker compose up --build
```

Puis ouvrir `http://127.0.0.1:8000/`.

Au premier lancement (si la base est vide) :
- applique automatiquement les migrations
- ajoute **15 produits** via `seed_products`

## Scénarios de test (rapide)

### Produits
- Ouvrir `/` : liste paginée
- Créer un produit : `/products/new/`
- Modifier un produit : `/products/<id>/edit/`
- Supprimer un produit : `/products/<id>/delete/`
- Pagination : créer **11** produits et vérifier qu’un lien “Suivant” apparaît

### Factures
- Créer une facture : `/invoices/new/`
  - cas normal : 1 à N lignes (produit + quantité)
  - erreurs : aucune ligne / doublon produit / ligne incomplète
- Liste des factures : `/invoices/` (pagination si > 10)
- Détail facture : `/invoices/<id>/`
  - lignes (produit, prix, quantité, sous-total)
  - **nombre total de produits**
  - **total à payer**

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

- Injecter 15 produits (local) :

```bash
python manage.py seed_products
```

