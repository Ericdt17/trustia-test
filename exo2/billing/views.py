from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import ProductForm
from .models import Product

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
