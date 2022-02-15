from django.views.generic import ListView, TemplateView, DetailView
from indexing.models import Product


class Index(ListView):
    """ Главная страница сайта """
    model = Product
    context_object_name = 'product'
    template_name = 'index/index.html'


class Shop(ListView):
    """ Страница магазина """
    model = Product
    context_object_name = 'product'
    template_name = 'index/shop-3-column.html'


class Contact(TemplateView):
    """ Страница контактной формы """
    template_name = 'index/contact.html'


class ProductDetailView(DetailView):
    """ Страница детального просмотра товара """
    model = Product
    context_object_name = 'product'
    template_name = 'index/shop-single-product.html'
