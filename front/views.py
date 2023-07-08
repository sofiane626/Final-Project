from django.shortcuts import render
from user.models import User
from product.models import Product, Category
from blog.models import Article, CategoryArticle
from contact.models import Contact
from django.db.models import Count

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
    category_id = request.GET.get('category_id')
    search_query = request.GET.get('q')

    if category_id == "tous":
        articles = Article.objects.all()
    elif category_id is not None:
        category = CategoryArticle.objects.get(pk=category_id)
        articles = Article.objects.filter(category=category)
    else:
        articles = Article.objects.all()

    # Filtrer les articles en fonction du nom recherché (search_query)
    if search_query:
        articles = articles.filter(title__icontains=search_query)

    categories = CategoryArticle.objects.all()

    # Récupérer les articles avec le plus de commentaires
    popular_articles = Article.objects.annotate(comment_count=Count('note2')).order_by('-comment_count')[:3]

    # Vérifier s'il y a des articles avec des commentaires
    if len(popular_articles) == 0:
        # Récupérer les trois premiers articles
        popular_articles = Article.objects.all()[:3]

    return render(request, 'Projet_Final/front/blog-5.html', {'articles': articles, 'categories': categories, 'popular_articles': popular_articles})


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