from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'joined_on')
    list_display_links = ('id', 'name')
    list_per_page = 20

admin.site.register(User, UserAdmin)