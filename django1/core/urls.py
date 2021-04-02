from django.urls import path
from .views import index, contact, product

# o segundo argumento é o nome da view/método
urlpatterns = [
    path('', index, name="index"),
    path('contact', contact, name="contact"),
    path('product/<int:id>', product, name="xuxa"),
]