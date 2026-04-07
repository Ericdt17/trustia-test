from django.contrib import admin

from .models import Invoice, InvoiceItem, Product


class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 0


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceItemInline]
    list_display = ("id", "created_at")
    ordering = ("-created_at",)


admin.site.register(Product)
