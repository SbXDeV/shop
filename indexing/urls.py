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
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('logout/', authViews.LogoutView.as_view(next_page='/'), name='exit'),
    path('profile/', views.Profile.as_view(), name='profile'),
    # Корзина
    path('detail', views.cart_detail, name='cart_detail'),
    path('add/(<product_id>)/', views.cart_add, name='cart_add'),
    path('remove/<product_id>)/', views.cart_remove, name='cart_remove'),
    # Магазинные страницы
    path('shop/categoryQ=1', views.ShopCategoryClutch.as_view(), name='clutch'),
    path('shop/categoryQ=2', views.ShopCategoryGame.as_view(), name='game'),
    path('shop/categoryQ=3', views.ShopCategoryPussy.as_view(), name='pussy'),
    path('shop/categoryQ=4', views.ShopCategoryAccess.as_view(), name='access'),
    path('shop/categoryQ=5', views.ShopCategoryPeople.as_view(), name='people'),
    path('shop/categoryQ=6', views.ShopCategoryRadio.as_view(), name='radio'),
    path('shop/categoryQ=7', views.ShopCategoryGamePass.as_view(), name='gamepass'),
    path('shop/categoryQ=8', views.ShopCategoryEvent.as_view(), name='event'),
]
