from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    image=models.ImageField( upload_to= 'media')

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    image=models.ImageField( upload_to= 'media')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=50) 
    email = models.EmailField(max_length=25)
    body = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.author