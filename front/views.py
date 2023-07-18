from django.shortcuts import render, redirect
from user.models import User
from product.models import Product, Category, CartItem, Cart
from blog.models import Article, CategoryArticle
from contact.models import Contact
from django.db.models import Count
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    contacts = Contact.objects.all()
    cart_items = CartItem.objects.all()
    products = Product.objects.order_by('-id')[:6]
    allProducts = Product.objects.all()
    popular_products = Product.objects.annotate(comment_count=Count('note')).order_by('-comment_count')[:6]
    latest_articles = Article.objects.all().order_by('-id')[:3]
    return render(request, 'Projet_Final/front/home.html', {'contacts' : contacts, 'products': products, "cart_items": cart_items, 'popular_products': popular_products, 'latest_articles': latest_articles, 'allProducts' : allProducts})

def product(request, category_id=None):
    products = Product.objects.all()
    active_category = None
    
    if category_id is not None:
        category = Category.objects.get(id=category_id)
        products = products.filter(category=category)
        active_category = category
    
    categories = Category.objects.all()
    
    paginator = Paginator(products, 12)  # Spécifiez le nombre de produits par page (ici, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'Projet_Final/front/products-left-sidebar-2.html', {
        'products': page_obj,
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




def checkout(request):
    cart_items = []
    total = 0
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = cart.cartitem_set.all()
        
        for cart_item in cart_items:
            cart_item.total = cart_item.quantity * cart_item.product.price
            total += cart_item.total
    
    # Récupérez la variable 'show' en fonction de votre logique d'affichage
    show = Product.objects.get(id=1)  # Remplacez 1 par votre logique de récupération du produit à afficher
    
    return render(
        request,
        'Projet_Final/front/checkout.html',
        {"cart_items": cart_items, "total": total, "show": show}
    )

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

def cart(request):
    cart_items = CartItem.objects.all()[:4]
    total = 0  # Variable pour stocker le total de la commande
    for item in cart_items:
        item.total = item.product.price * item.quantity
        total += item.total  # Accumuler le sous-total à chaque itération
    allProducts = Product.objects.all()
    return render(request, 'Projet_Final/front/cart.html', {'allProducts': allProducts, "cart_items": cart_items, "total": total})

def update_wish(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        wish = request.POST.get('wish')

        # Effectuez les modifications nécessaires dans votre base de données Django
        # par exemple, en utilisant le modèle Product et en mettant à jour l'attribut 'wish' du produit correspondant
        product = Product.objects.get(id=product_id)
        product.wish = wish
        product.save()

    return redirect('home')  # Redirigez l'utilisateur vers la vue souhaitée après la mise à jour