from django.conf import settings
from django.urls import path, include
from . views import dashboard, test

urlpatterns = [
        path('', dashboard, name='dashboard'),  
        path('test/', test, name='test')


]