from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Ticket(models.Model):
    
    TICKET_TYPE = (
        ('Bug', 'Bug Report'),
        ('Feature', 'Feature Request'),
    )
    
    TICKET_STATUS = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Complete', 'Complete'),
    )
    
    userid = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=250)
    description = models.TextField()
    url = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    type = models.CharField(max_length=20, choices=TICKET_TYPE, blank=False)
    status = models.CharField(max_length=20, choices=TICKET_STATUS, default='Pending')
    created_on = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.title