from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import ListView, TemplateView, DetailView, FormView

from indexing.cart import Cart
from indexing.forms import LoginForm, CartAddProductForm
from indexing.models import Product, Police, Transport, Sale


class Index(ListView):
    """ Главная страница сайта """
    template_name = 'main/index.html'

    def get(self, request):
        cart = Cart(request)
        sales = Sale.objects.all()
        product = Product.objects.all()
        return render(request, 'main/index.html', {'sales': sales, 'product': product, 'cart': cart})


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


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return redirect('/profile', {'username': username, })
            else:
                form.add_error(None, 'Неверный логин или пароль, проверьте введенные вами данные')
                return render(request, 'auth/login-register.html', {'form': form})
        else:
            return render(request, 'auth/login-register.html', {'form': form})
    else:
        return render(request, 'auth/login-register.html', {'form': LoginForm()})


class Profile(TemplateView):
    template_name = 'auth/my-account.html'


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('indexing:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('indexing:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/shop-checkout.html', {'cart': cart})
