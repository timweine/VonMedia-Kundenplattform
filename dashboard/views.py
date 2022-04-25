from django.shortcuts import render
from django.http import HttpResponse
from . models import Brand_Logo


def dashboard(request):
    html = '<h1>Dashboard</h1>'
    return render(request, 'pages\dashboard.html')

    'pages\dashboard.html'


def test(request):
    
    context = Brand_Logo.objects.all
    print( 'context print' )
    print (context)
    return HttpResponse('asdfsadfa')