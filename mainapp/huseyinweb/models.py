from django.db import models
from django.forms import ModelForm, TextInput

# Create your models here.

class Project(models.Model):
     title = models.CharField(max_length=50)
     description = models.TextField()
     detail_link = models.CharField(max_length=250)
     image = models.ImageField(upload_to='projects')
     
     def __str__(self):
          return self.title
     
class Skill(models.Model):
     title = models.CharField(max_length=50)
     description = models.TextField()
     
     def __str__(self):
          return self.title
     
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    message = models.TextField()
    
    def __str__(self):
        return self.name 