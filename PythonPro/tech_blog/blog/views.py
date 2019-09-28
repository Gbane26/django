from django.shortcuts import render
from . models import *

# Create your views here.

def home(request):
    context = {
        'category': Category.objects.all(),
        'article': Article.objects.all(),
        'commentaire': Commentaire.objects.all(),
    }
    return render(request, 'pages/tech-index.html', context)

def author(request):
    return render(request, 'pages/tech-author.html')

def category1(request):
    context = {
        'article': Article.objects.all(),
    }
    return render(request, 'pages/tech-category-01.html', context)

def category2(request):
    return render(request, 'pages/tech-category-02.html')

def category3(request):
    return render(request, 'pages/tech-category-03.html')

def contact(request):
    return render(request, 'pages/tech-contact.html')

def single(request):
    context = {
        
        'category': Category.objects.all(),
        'article': Article.objects.all(),
        'commentaire': Commentaire.objects.all(),
    }
    return render(request, 'pages/tech-single.html')


    
