#!/usr/bin/env sh
set -eu

python manage.py migrate --noinput

# Si la base est vide, on ajoute 15 produits de démo
python manage.py shell -c "from billing.models import Product; raise SystemExit(0 if Product.objects.exists() else 1)" \
  || python manage.py seed_products --count 15

exec python manage.py runserver 0.0.0.0:8000

