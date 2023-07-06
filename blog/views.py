from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.

def updateArticle(request,id):
    edit = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('back_Article')
    else:
        form = ArticleForm(instance=edit)
    return render(request, 'Projet_Final/back/back_edit.html', {'form': form})

def destroy_Article(request, id):
    destroy = Article(id)
    destroy.delete()
    return redirect('back_Article')

def createArticle(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('back_Article')
    else:
        form = ArticleForm()
    return render(request, 'Projet_Final/back/back_edit.html', {"form": form})
