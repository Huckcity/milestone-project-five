from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from tickets.models import Ticket
from blog.models import Post

class Comment(models.Model):

    userid = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ticketid = models.ForeignKey(Ticket, blank=True, null=True, on_delete=models.CASCADE)
    blog_post_id = models.ForeignKey(Post, blank=True, null=True, on_delete=models.CASCADE)
    comment = models.TextField(blank=False)
    posted_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.comment
