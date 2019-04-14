from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    published_on = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def publish(self):
        self.published_on = timezone.now()
        self.save()

    def __str__(self):
        return self.title
