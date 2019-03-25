from django.contrib import admin

from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('userid', 'userid', 'comment', 'posted_on')
    list_display_links = ('comment',)
    # list_filter = ('status', 'type')
    list_per_page = 20

admin.site.register(Comment, CommentAdmin)