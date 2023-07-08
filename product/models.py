from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from user.models import User

class Category(models.Model):
    value = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.value


class Product(models.Model):
    img1 = models.CharField(max_length=1000)
    img2 = models.CharField(max_length=1000)
    img3 = models.CharField(max_length=1000)
    description = models.TextField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    price = models.PositiveIntegerField()
    promo = models.PositiveIntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    tailleS = models.IntegerField()
    tailleM = models.IntegerField()
    tailleL = models.IntegerField()
    tailleXL = models.IntegerField()

class Note(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    anonymous_author = models.ForeignKey('AnonymousUser', null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    titre = models.CharField(max_length=50)
    text = models.TextField(max_length=300, default='valeur_par_défaut')


class AnonymousUser(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()



class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    # entre progress / noValidate / validate
    status = models.CharField(max_length=50)

class Achat(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
