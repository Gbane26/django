from django.urls import path 
from hello_world import views


urlpatterns = [
    path('', views.helloworld, name="helloworld"),
    path('page', views.page, name="page"),
]
