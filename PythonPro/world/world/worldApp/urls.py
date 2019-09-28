from django.urls import path 
from worldApp import views

urlpatterns = [
    path('', views.worldapp, name="worldapp"),
    # path('page', views.page, name="page"),
]
