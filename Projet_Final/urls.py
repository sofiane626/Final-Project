"""
URL configuration for Projet_Final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from front.views import *
from user.views import *
from product.views import *
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('product/', product, name='product'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('connexion/', connexion, name='login'),
    path('inscription/', inscription, name='signup'),
    path('logout/', deco ),
    path('checkout/', checkout, name='checkout'),
    path('backoffice/', backoffice, name='backoffice'),
    path('user/destroy/<int:id>', destroy_User),
    path('user/edit/<int:id>', updateUser),
    path('back_product/', back_product, name='back_product'),
    path('product/edit/<int:id>', updateProduct),
    path('product/destroy/<int:id>', destroy_Product),
    path('create/product/', createProduct, name='create_Product'),
    path('equipe/<int:id>', readProduct, name='detail_Product'),
    path('back_article/', back_article, name='back_article'),
    path('article/edit/<int:id>', updateArticle),
    path('article/destroy/<int:id>', destroy_Article),
    path('create/article/', createArticle, name='create_article'),
]
