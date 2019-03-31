"""
Models for Ticket system
"""

from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    """
    Model for tickets, which accommodate for both bug reports and feature requests
    """

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
    price = models.DecimalField(max_digits=5,
                                decimal_places=2,
                                blank=True,
                                null=True,
                                default=50.00)
    type = models.CharField(max_length=20, choices=TICKET_TYPE, blank=False)
    status = models.CharField(max_length=20, choices=TICKET_STATUS, default='Pending')
    created_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

class Contribution(models.Model):
    """
    Contributions model for tracking amounts committed to feature development
    """

    userid = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ticket = models.ForeignKey(Ticket, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=5,
                                 decimal_places=2,
                                 blank=False)
    contributed_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.userid.username
