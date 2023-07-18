from django.db import models

# Create your models here.

class Contact(models.Model):
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    fax = models.CharField(max_length=20)

    def __str__(self):
        return self.location
    
class Contact_mail(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)
    
    def toggle_read(self):
        self.read = not self.read
        self.save()

class Reply(models.Model):
    to = models.ForeignKey(Contact, on_delete=models.CASCADE)
    content = models.TextField()