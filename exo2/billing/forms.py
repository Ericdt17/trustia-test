from django import forms
from django.core.exceptions import ValidationError
from django.forms import BaseModelFormSet, modelformset_factory

from .models import InvoiceItem, Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "price", "expiry_date")
        widgets = {
            "expiry_date": forms.DateInput(attrs={"type": "date"}),
        }

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price <= 0:
            raise ValidationError("Le prix doit être strictement positif.")
        return price


class BaseInvoiceItemFormSet(BaseModelFormSet):
    def clean(self):
        super().clean()
        if any(self.errors):
            return

        products = []
        filled_rows = 0
        for form in self.forms:
            if not form.cleaned_data:
                continue
            product = form.cleaned_data.get("product")
            quantity = form.cleaned_data.get("quantity")
            if product is None and quantity is None:
                continue
            if product is None or quantity is None:
                raise ValidationError("Chaque ligne doit avoir un produit et une quantité.")
            filled_rows += 1
            if product.pk in products:
                raise ValidationError(
                    "Un même produit ne peut apparaître qu'une seule fois sur la facture."
                )
            products.append(product.pk)

        if filled_rows == 0:
            raise ValidationError("Ajoutez au moins une ligne avec un produit et une quantité.")


InvoiceItemFormSet = modelformset_factory(
    InvoiceItem,
    fields=("product", "quantity"),
    extra=3,
    min_num=0,
    validate_min=False,
    formset=BaseInvoiceItemFormSet,
)
