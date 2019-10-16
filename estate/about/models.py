from django.db import models

# Create your models here.


class About(models.Model):
    titre = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titre

class Agenda(models.Model):
    titre = models.CharField(max_length=255)
    number = models.CharField(max_length=255)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titre

class About_image(models.Model):
    image = models.ImageField(upload_to='img')

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

class Team(models.Model):
    nom = models.CharField(max_length=255)
    fontion=models.CharField(max_length=255)
    description=models.TextField()
    image = models.ImageField(upload_to='img')
    
    def __str__(self):
        return self.nom