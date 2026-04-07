from __future__ import annotations

import random
from datetime import timedelta
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.utils import timezone

from billing.models import Product


class Command(BaseCommand):
    help = "Seed the database with demo products."

    def add_arguments(self, parser):
        parser.add_argument("--count", type=int, default=15, help="Number of products to create.")
        parser.add_argument(
            "--prefix",
            type=str,
            default="Produit",
            help="Name prefix used for generated products.",
        )

    def handle(self, *args, **options):
        count: int = options["count"]
        prefix: str = options["prefix"]

        today = timezone.localdate()
        products: list[Product] = []

        store_names = [
            "lait demi-écrémé 1L",
            "œufs x12",
            "pâtes spaghetti 500g",
            "riz basmati 1kg",
            "farine 1kg",
            "sucre 1kg",
            "huile d'olive 1L",
            "beurre 250g",
            "yaourt nature x8",
            "jambon blanc x4",
            "fromage râpé 200g",
            "tomates 1kg",
            "pommes 1kg",
            "bananes 1kg",
            "eau minérale 6x1.5L",
        ]

        for i in range(1, count + 1):
            base_name = store_names[i - 1] if i <= len(store_names) else f"{prefix} {i:03d}"
            cents = random.randint(99, 9999)  # 0.99 -> 99.99
            price = (Decimal(cents) / Decimal(100)).quantize(Decimal("0.01"))
            expiry_date = today + timedelta(days=random.randint(1, 365))

            products.append(Product(name=base_name, price=price, expiry_date=expiry_date))

        Product.objects.bulk_create(products)
        self.stdout.write(self.style.SUCCESS(f"Created {count} products."))

