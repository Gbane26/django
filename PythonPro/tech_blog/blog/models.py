from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    image=models.ImageField( upload_to= 'media')
    statut=models.BooleanField(default=True)
    date_add=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Article(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    author= models.CharField(max_length=255)
    image=models.ImageField( upload_to= 'media')
    statut=models.BooleanField(default=True)
    date_add=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)
    Category_id= models.ForeignKey(Category, on_delete=models.CASCADE, related_name="Article_Category")

    def __str__(self):
        return self.title

class Commentaire(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE, related_name="User_Commentaire") 
    description=models.TextField()
    image=models.ImageField( upload_to= 'media')
    statut=models.BooleanField(default=True)
    date_add=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)
    Article_Id=models.ForeignKey(Article, on_delete=models.CASCADE, related_name="Commentaire_Article")
    
    def __str__(self):
        return self.title
    