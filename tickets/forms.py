"""
Ticketeting Forms
"""

from django import forms

from .models import Ticket

class AddBug(forms.ModelForm):
    """
    Form for adding bugs tickets
    """
    class Meta:
        model = Ticket
        fields = ('title', 'description', 'url', 'image', )

class AddFeature(forms.ModelForm):
    """
    Form for adding feature tickets
    """
    class Meta:
        model = Ticket
        fields = ('title', 'description', 'url', 'price', )
        