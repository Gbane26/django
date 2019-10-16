from django.db import models

# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=255)
    statut=models.BooleanField(default=True)
    date_add=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Tag(models.Model):
    title=models.CharField(max_length=255)
    statut=models.BooleanField(default=True)
    date_add=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title



class Article(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    image=models.ImageField( upload_to= 'media')
    video=models.CharField(max_length=255)
    statut=models.BooleanField(default=True)
    date_add=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)
    Category_id= models.ForeignKey(Category, on_delete=models.CASCADE, related_name="Article_Category")
    Category_id= models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="Article_Tag")

    def __str__(self):
        return self.title