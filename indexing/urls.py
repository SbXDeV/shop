from django.urls import path
from . import views

app_name = 'indexing'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('contact', views.Contact.as_view(), name='contact'),
]
