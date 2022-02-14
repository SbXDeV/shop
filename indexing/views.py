from django.views.generic import ListView, TemplateView, DetailView
from indexing.models import Product


class Index(ListView):
    model = Product
    context_object_name = 'product'
    template_name = 'index/index.html'


class Contact(TemplateView):
    template_name = 'index/contact.html'


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'index/shop-single-product.html'
