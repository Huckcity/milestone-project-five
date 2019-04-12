"""
URLS for Tickets App
"""
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^bugs$', views.bugs, name='bugs'),
    url(r'^bug/(?P<bugid>\d+)/$', views.bug, name='bug'),
    url(r'^features$', views.features, name='features'),
    url(r'^feature/(?P<featureid>\d+)/$', views.feature, name='feature'),
    url(r'^addbug', views.addbug, name='addbug'),
    url(r'^addfeature', views.addfeature, name='addfeature'),
    url(r'^addvote/(?P<bugid>\d+)/$', views.addvote, name='addvote'),
]
