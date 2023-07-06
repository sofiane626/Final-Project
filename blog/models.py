from django.db import models
from user.models import User

class CategoryArticle(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag


class Article(models.Model):
    title = models.CharField(max_length=100)
    img = models.CharField(max_length=1000)
    description = models.TextField()
    category = models.ForeignKey(CategoryArticle, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    validate = models.BooleanField(default=False)

    def __str__(self):
        return self.title
