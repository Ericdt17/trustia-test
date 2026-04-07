from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import InvoiceItemFormSet, ProductForm
from .models import Invoice, InvoiceItem, Product

PAGINATE_BY = 10


class ProductListView(ListView):
    model = Product
    context_object_name = "products"
    paginate_by = PAGINATE_BY


class ProductCreateView(SuccessMessageMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("billing:product_list")
    success_message = "Produit créé."


class ProductUpdateView(SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("billing:product_list")
    success_message = "Produit mis à jour."


class ProductDeleteView(SuccessMessageMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("billing:product_list")
    success_message = "Produit supprimé."


class InvoiceListView(ListView):
    model = Invoice
    context_object_name = "invoices"
    paginate_by = PAGINATE_BY
    ordering = ["-created_at"]


class InvoiceCreateView(View):
    template_name = "billing/invoice_form.html"

    def get(self, request):
        formset = InvoiceItemFormSet(queryset=InvoiceItem.objects.none())
        return render(request, self.template_name, {"formset": formset})

    def post(self, request):
        formset = InvoiceItemFormSet(request.POST, queryset=InvoiceItem.objects.none())
        if formset.is_valid():
            invoice = Invoice.objects.create()
            for obj in formset.save(commit=False):
                obj.invoice = invoice
                obj.save()
            messages.success(request, "Facture créée.")
            return redirect("billing:invoice_list")
        return render(request, self.template_name, {"formset": formset})


class InvoiceDetailView(DetailView):
    model = Invoice
    context_object_name = "invoice"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["items"] = self.object.items.select_related("product")
        return ctx
