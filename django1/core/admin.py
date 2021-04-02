from django.contrib import admin

# Register your models here.

from .models import Product, Client

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock")

class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "email")
admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)