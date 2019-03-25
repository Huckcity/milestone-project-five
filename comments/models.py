from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from tickets.models import Ticket


class Comment(models.Model):
    
    userid = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ticketid = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    comment = models.TextField(blank=False)
    posted_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.comment