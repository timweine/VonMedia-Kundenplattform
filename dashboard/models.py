from django.db import models
from accounts.models import CustomUser

 
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    price = models.FloatField(max_length=100)
    is_featured = models.BooleanField(default=False)

class Brand(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=255)

class Brand_Asset(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

class Brand_Logo(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    logo = models.ImageField(null=True, blank=True, upload_to='media/brands/logos')
    
    

class Order(models.Model):

    STATUS_CHOICES = (
        ("pending", "pending"),
        ("confirmed", "confirmed"),
        ("completed", "completed")
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default = 'pending')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

