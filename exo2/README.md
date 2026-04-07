# Exercice 2 — Django (Produits & Factures)

## Lancer le projet

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

Les **totaux agrégés** (somme des quantités, montant total à payer) peuvent être ajoutés dans une étape suivante.

## Modèles (base de données)

- `Product`: `name`, `price`, `expiry_date`
- `Invoice`
- `InvoiceItem`: lien Facture ↔ Produit + `quantity`

## À implémenter ensuite

- Page détail facture : **total quantités** et **total à payer** (agrégats)
