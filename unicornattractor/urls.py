from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'', include('pages.urls')),
    url(r'admin/', admin.site.urls),
    url(r'accounts/', include('accounts.urls')),
    url(r'tickets/', include('tickets.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
