from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def blog(request):
    return render(request, 'pages/blog.html')

def contact(request):
    return render(request, 'pages/contact.html')

def developments(request):
    return render(request, 'pages/developments.html')

def property(request):
    return render(request, 'pages/property.html')