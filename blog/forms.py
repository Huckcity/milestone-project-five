"""
Blog Forms
"""

from django import forms

from .models import Post

class AddPost(forms.ModelForm):
    """
    Form for adding blog posts
    """
    class Meta:
        model = Post
        fields = ('title', 'body', )
