from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.bugs, name='bugs'),
    url(r'^bugs$', views.bugs, name='bugs'),
    url(r'^features', views.features, name='features'),
    url(r'^addticket', views.addticket, name='addticket'),
    ]