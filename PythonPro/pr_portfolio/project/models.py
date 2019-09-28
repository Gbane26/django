from django.db import models

# Create your models here.

class Project(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    image=models.ImageField( upload_to= 'media')
    date_add=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)
    tecnology=models.CharField(max_length=250)

    def __str__(self):
        return self.title
    

class Project_detail(models.Model):
    Project_id= models.ForeignKey(Project, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.TextField()
    image=models.FileField( upload_to= 'media')
    date_add=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)
    tecnology=models.CharField(max_length=250)

    def __str__(self):
        return self.title
    
   
        