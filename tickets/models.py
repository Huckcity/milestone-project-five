from django.db import models
from datetime import datetime

from accounts.models import User

class Ticket(models.Model):
    
    userid = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=250)
    description = models.TextField()
    url = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images', blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    type = models.CharField(max_length=250)
    status = models.CharField(max_length=250, default="To Do")
    created_on = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.title