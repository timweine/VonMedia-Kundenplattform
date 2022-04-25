from django.contrib import admin
from . models import Product, Order , Brand , Brand_Logo
# Register your models here.

admin.site.register(Brand)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Brand_Logo)