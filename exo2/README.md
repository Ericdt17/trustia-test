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

## Modèles (base de données)
- `Product`: `name`, `price`, `expiry_date`
- `Invoice`
- `InvoiceItem`: lien Facture ↔ Produit + `quantity`

## TODO (fonctionnel)
Il reste à implémenter :
- CRUD produits (avec pagination)
- Création facture + sélection produits + quantités
- Page détail facture (liste items, total quantités, total à payer)

