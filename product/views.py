from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

def updateProduct(request,id):
    edit = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('back_product')
    else:
        form = ProductForm(instance=edit)
    return render(request, 'Projet_Final/back/back_edit.html', {'form': form})

def destroy_Product(request, id):
    destroy = Product(id)
    destroy.delete()
    return redirect('back_product')

def createProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('back_product')
    else:
        form = ProductForm()
    return render(request, 'Projet_Final/back/back_edit.html', {"form": form})


def readProduct(request, id):
    show = Product.objects.get(id=id)
    notes = Note.objects.filter(product=id)
    
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        
        if not request.user.is_authenticated:
            # Rediriger vers la page de connexion en conservant l'URL de redirection
            login_url = reverse('login')
            return redirect(f'{login_url}?next={request.path}')
        
        cart, created = Cart.objects.get_or_create(user=request.user)
        
        # Récupérer la valeur de la taille depuis la requête POST
        size = request.POST.get('size')
        
        # Vérifier si la taille est définie et attribuer une valeur par défaut si elle est None
        if size is None:
            size = 'S'  # Ou une autre valeur par défaut
        
        if 'remove_item' in request.POST:
            remove_item_id = int(request.POST['remove_item'])
            remove_item = CartItem.objects.get(id=remove_item_id)
            
            # Restaurer le stock du produit correspondant
            remove_item.restore_stock()
            
            # Supprimer l'article du panier
            remove_item.delete()
        else:
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=show, size=size)
            
            # Vérifier si la quantité ajoutée dépasse le stock disponible
            stock_available = show.stock
            if quantity > stock_available:
                quantity = stock_available  # Réduire la quantité au stock disponible
            
            # Si le CartItem existe déjà, mettez à jour la quantité plutôt que de créer un nouveau CartItem
            if not created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity
            
            cart_item.save()
            
            # Mettre à jour le stock du produit
            show.stock -= quantity
            show.save()
        
        # Rediriger vers la page du produit après l'ajout ou la suppression de l'article
        return redirect('detail_Product', id=id)
    
    cart_items = []
    total = 0
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = cart.cartitem_set.all()
        total = sum(item.quantity * item.product.price for item in cart_items)
    
    return render(
        request,
        'Projet_Final/front/products-type-1.html',
        {"show": show, "notes": notes, "cart_items": cart_items, "total": total}
    )

def cart_view(request):
    # try:
    #     cart = Cart.objects.get(user=request.user)
    #     cart_items = cart.cartitem_set.all()
    #     context = {'cart': cart, 'cart_items': cart_items}
    # except Cart.DoesNotExist:
    #     context = {'cart': None, 'cart_items': None}

    cart_items = CartItem.objects.all()[0]
    
    return render(request, 'Projet_Final/front/cart.html', {"cart_items": cart_items})

def comment_create(request, id):
    if request.method == 'POST':
        product = Product.objects.get(id=id)
        titre = request.POST.get('review-title')
        text = request.POST.get('texte')
        
        if request.user.is_authenticated:
            current_note = Note.objects.create(
                author=request.user,
                product=product,
                titre=titre,
                text=text
            )
        else:
            name = request.POST.get('name')
            email = request.POST.get('email')
            
            anonymous_user = AnonymousUser.objects.create(
                name=name,
                email=email
            )
            
            current_note = Note.objects.create(
                anonymous_author=anonymous_user,
                product=product,
                titre=titre,
                text=text
            )
        
        return redirect('detail_Product', id=id)
    
    return render(request, 'Projet_Final/front/products-type-1.html')
   
