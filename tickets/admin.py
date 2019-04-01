"""
Register ticketing modules within admin panel
"""
from django.contrib import admin

from .models import Ticket, Contribution, Vote

class TicketAdmin(admin.ModelAdmin):
    """
    Register tickets within admin panel
    """
    list_display = ('id', 'title', 'userid', 'created_on', 'type', 'status')
    list_display_links = ('id', 'title')
    list_filter = ('status', 'type')
    list_per_page = 20

class ContribAdmin(admin.ModelAdmin):
    """
    Register contributions within admin panel
    """
    list_display = ('id', 'userid', 'contributed_on')

class VoteAdmin(admin.ModelAdmin):
    """
    Register votes in admin panel
    """
    list_display = ('id', 'user', 'ticket')
    list_display_links = ('user', 'ticket')

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Contribution, ContribAdmin)
admin.site.register(Vote, VoteAdmin)
