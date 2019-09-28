from django.shortcuts import render
from .models import *

# Create your views here.

def project_index(request):
    context = {
        'project': Project.objects.all()
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    context = {
        'detail': Project_detail.objects.get(pk=pk)
    }
    return render(request, 'project_detail.html', context)