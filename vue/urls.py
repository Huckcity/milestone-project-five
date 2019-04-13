from django.conf.urls import include
from django.urls import path
from django.views.generic import TemplateView

from rest_framework import routers

from tickets.viewsets import TicketViewSet


router = routers.DefaultRouter()
router.register('tickets', TicketViewSet, 'tickets')

urlpatterns = [
    path('', TemplateView.as_view(template_name='vue/vue_index.html')),
    path('api/', include(router.urls)),
]