from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from user.models import User
from django.utils import timezone

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
    stock = models.IntegerField(default=0)
    def get_stock(self):
        return self.stock

class Note(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    anonymous_author = models.ForeignKey('AnonymousUser', null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    titre = models.CharField(max_length=50)
    text = models.TextField(max_length=300, default='valeur_par_défaut')


class AnonymousUser(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()



class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')
    
    def __str__(self):
        return f"Cart for {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=2, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    
    def restore_stock(self):
        self.product.stock += self.quantity
        self.product.save()

class Order(models.Model):
    STATUS_CHOICES = (
        ('novalidate', 'Non validée'),
        ('validate', 'Validée'),
        ('progress', 'En cours de traitement'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, default=None)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='novalidate')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"