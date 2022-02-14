from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView
from indexing.models import Product


class Index(ListView):
    model = Product
    context_object_name = 'product'
    template_name = 'index/index.html'


class Contact(TemplateView):
    template_name = 'index/contact.html'
