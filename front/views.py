from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'Projet_Final/front/home.html')

def product(request):
    return render(request, 'Projet_Final/front/products-left-sidebar-2.html')

def blog(request):
    return render(request, 'Projet_Final/front/blog-5.html')

def contact(request):
    return render(request, 'Projet_Final/front/contact.html')

def connexion(request):
    return render(request, 'Projet_Final/front/login.html')

