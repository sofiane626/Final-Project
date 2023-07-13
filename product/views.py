from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponseBadRequest

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
    notes = Note.objects.all().filter(product=id)
    show = Product.objects.get(id=id)
    
    # Stock par taille
    stock = {
        'S': show.tailleS,
        'M': show.tailleM,
        'L': show.tailleL,
        'XL': show.tailleXL,
    }
    
    return render(
        request,
        'Projet_Final/front/products-type-1.html',
        {"show": show, "notes": notes, "stock": stock}
    )


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
   
