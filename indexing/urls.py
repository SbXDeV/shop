from django.urls import path
from . import views

app_name = 'indexing'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('contact', views.Contact.as_view(), name='contact'),
    path('shop/', views.Shop.as_view(), name='shop'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
]
