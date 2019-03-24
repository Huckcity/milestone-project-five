from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    photo = models.ImageField(upload_to='photos', blank=True)
    bio = models.TextField(blank=True)
    joined_on = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.name