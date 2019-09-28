from django.shortcuts import render

# Create your views here.
def helloworld(request):
	return render(request, 'hello_world.html')

def page(request):
	return render(request, 'page.html')