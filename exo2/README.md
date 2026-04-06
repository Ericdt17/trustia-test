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

## Modèles (base de données)

- `Product`: `name`, `price`, `expiry_date`
- `Invoice`
- `InvoiceItem`: lien Facture ↔ Produit + `quantity`

## À implémenter ensuite

- Création facture + sélection produits + quantités
- Page détail facture (liste items, total quantités, total à payer)
