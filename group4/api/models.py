from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img')
    status = models.BooleanField()
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom


class SousCategorie(models.Model):
    categorie = models.ForeignKey(Categorie, related_name='souscategories', on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img')
    status = models.BooleanField()
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

class Article(models.Model):
    sousCategorie = models.ForeignKey(SousCategorie, related_name='article_cat', on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img')
    status = models.BooleanField()
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

class Commentaire(models.Model):
    article = models.ForeignKey(Article, related_name='article_commentaire', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='article_commentaire', on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    status = models.BooleanField()
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now=True)
