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
        parser.add_argument("--count", type=int, default=50, help="Number of products to create.")
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

        for i in range(1, count + 1):
            name = f"{prefix} {i:03d}"
            cents = random.randint(99, 9999)  # 0.99 -> 99.99
            price = (Decimal(cents) / Decimal(100)).quantize(Decimal("0.01"))
            expiry_date = today + timedelta(days=random.randint(1, 365))

            products.append(Product(name=name, price=price, expiry_date=expiry_date))

        Product.objects.bulk_create(products)
        self.stdout.write(self.style.SUCCESS(f"Created {count} products."))

