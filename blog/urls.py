from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.all_posts, name='blog'),
    url(r'^post/(?P<post_id>\d+)/$', views.single_post, name='post'),
    url(r'^addpost/$', views.add_post, name='addpost'),
]
