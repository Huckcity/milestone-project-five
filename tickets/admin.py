from django.contrib import admin

from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_on', 'type', 'status')
    list_display_links = ('id', 'title')
    list_filter = ('status', 'type')
    list_per_page = 20

admin.site.register(Ticket, TicketAdmin)