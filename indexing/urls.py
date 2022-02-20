from django.urls import path, include
from . import views
from django.contrib.auth import views as authViews

app_name = 'indexing'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('contact', views.Contact.as_view(), name='contact'),
    path('politic', views.Politic.as_view(), name='police'),
    path('about-transport', views.Transfer.as_view(), name='transport'),
    path('shop/', views.Shop.as_view(), name='shop'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    # Авторизация
    path('login/', views.user_login, name='login'),
    path('logout/', authViews.LogoutView.as_view(next_page='/'), name='exit'),
    path('profile/', views.Profile.as_view(), name='profile'),
    # Корзина
    path('detail', views.cart_detail, name='cart_detail'),
    path('add/(<product_id>)/', views.cart_add, name='cart_add'),
    path('remove/<product_id>)/', views.cart_remove, name='cart_remove'),
]
