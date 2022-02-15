from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from indexing.models import Product, Police, Transport, Sale


class Index(ListView):
    """ Главная страница сайта """
    template_name = 'main/index.html'

    def get(self, request):
        sales = Sale.objects.all()
        product = Product.objects.all()
        return render(request, 'main/index.html',  {'sales': sales, 'product': product})


class Shop(ListView):
    """ Страница магазина """
    model = Product
    context_object_name = 'product'
    template_name = 'main/shop.html'


class Contact(TemplateView):
    """ Страница контактной формы """
    template_name = 'main/content.html'


class Politic(ListView):
    """ Страница политики конфиденциальности """
    model = Police
    context_object_name = 'police'
    template_name = 'main/politic.html'


class Transfer(ListView):
    """ Страница сведений о доставке """
    model = Transport
    context_object_name = 'police'
    template_name = 'main/transport.html'

class ProductDetailView(DetailView):
    """ Страница детального просмотра товара """
    model = Product
    context_object_name = 'product'
    template_name = 'main/detail.html'
