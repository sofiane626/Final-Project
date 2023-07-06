from django.shortcuts import render
from user.models import User
from product.models import Product

# Create your views here.

def home(request):
    return render(request, 'Projet_Final/front/home.html')

def product(request):
    products = Product.objects.all()
    return render(request, 'Projet_Final/front/products-left-sidebar-2.html', {'products' : products,})

def blog(request):
    return render(request, 'Projet_Final/front/blog-5.html')

def contact(request):
    return render(request, 'Projet_Final/front/contact.html')

def checkout(request):
    return render(request, 'Projet_Final/front/checkout.html')

def backoffice(request):
    users = User.objects.all()
    return render(request, 'Projet_Final/back/backoffice.html', {'users' : users,})

def back_product(request):
    products = Product.objects.all()
    return render(request, 'Projet_Final/back/back_product.html', {'products' : products,})
