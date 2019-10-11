from django.urls import path 
from . import views
urlpatterns = [
    path('', views.home, name="index"),
    path('index2', views.index2 , name="index2"),
    path('post', views.senddata , name="post"),
]
