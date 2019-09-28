from django.urls import path
from blog import views


urlpatterns = [
    path('', views.home, name="home"),
    path('author/', views.author, name="author"),
    path('single', views.single, name="single"),
    path('contact', views.contact, name="contact"),
    path('category1/', views.category1, name="category1"),
    path('category2', views.category2, name="category2"),
    path('category3', views.category3, name="category3"),
]
