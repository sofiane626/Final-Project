from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.hashers import make_password
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.



def inscription(request):
    if request.method == 'POST':
        username = request.POST['username']
        img_url = request.POST['img_url']
        password = request.POST['password']
        email = request.POST['email']
        user = User(username=username, password=make_password(password), email=email, img_url=img_url)
        user.save()
        login(request, user)
    return render(request, 'Projet_Final/front/signup.html')

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'Projet_Final/front/login.html')

def deco(request):
    logout(request)
    return redirect('home')

# def passwordchange(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)
#             send_mail('maj password', 'Ton mdp à été modifier', 'marouaneindustries@mail.com', [user.email])
#             return redirect('home')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'lerecap/coco/passwordchange.html', {'form': form})

def updateUser(request,id):
    edit = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('backoffice')
    else:
        form = UserForm(instance=edit)
    return render(request, 'Projet_Final/back/back_edit.html', {'form': form})

def destroy_User(request, id):
    destroy = User(id)
    destroy.delete()
    return redirect('backoffice')