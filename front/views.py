from django.shortcuts import render
from user.models import User
from product.models import Product, Category
from blog.models import Article
from contact.models import Contact

# Create your views here.

def home(request):
    contacts = Contact.objects.all()
    return render(request, 'Projet_Final/front/home.html', {'contacts' : contacts})

def product(request, category_id=None):
    products = Product.objects.all()
    active_category = None
    
    if category_id is not None:
        category = Category.objects.get(id=category_id)
        products = products.filter(category=category)
        active_category = category
    
    categories = Category.objects.all()
    
    return render(request, 'Projet_Final/front/products-left-sidebar-2.html', {
        'products': products,
        'categories': categories,
        'active_category': active_category
    })


def blog(request):
    return render(request, 'Projet_Final/front/blog-5.html')

def contact(request):
    contacts = Contact.objects.all()
    return render(request, 'Projet_Final/front/contact.html', {'contacts' : contacts})

def checkout(request):
    return render(request, 'Projet_Final/front/checkout.html')

def backoffice(request):
    users = User.objects.all()
    return render(request, 'Projet_Final/back/backoffice.html', {'users' : users,})

def back_product(request):
    products = Product.objects.all()
    return render(request, 'Projet_Final/back/back_product.html', {'products' : products,})

def back_article(request):
    articles = Article.objects.all()
    return render(request, 'Projet_Final/back/back_blog.html', {'articles' : articles,})

def back_contact(request):
    contacts = Contact.objects.all()
    return render(request, 'Projet_Final/back/back_contact.html', {'contacts' : contacts})