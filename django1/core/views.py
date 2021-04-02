from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    #print(dir(request))
    #print(f'Method: {request.method}')
    #print(f'Headers: {request.headers}')
    #print(f'User: {request.user}')
    #print(dir(request.user))
    
    if str(request.user) == "AnonymousUser":
        login = "User Not Logged In"
    else:
        login = "User Logged in"
        
    products = Product.objects.all()
    
    context = { "geek" : "Programacao Web Com Django Framework", 
               "curso" : "Engenharia Informatica",
               "login": login,
               "products": products,}
    return render(request, "index.html", context)


def contact(request):
    return render(request, "contact.html")


def product(request, id):
    print(f'ID: {id}')
    #p = Product.objects.get(id=id)
    p = get_object_or_404(Product, id=id)
    
    context = {"product" : p,
               }
    return render(request, "product.html", context)

def error404(request, exception):
    template = loader.get_template("404.html")
    return HttpResponse(content=template.render(), content_type="text/html; charset=utf-8", status=404)

def error500(request):
    template = loader.get_template("500.html")
    return HttpResponse(content=template.render(), content_type="text/html; charset=utf-8", status=500)
