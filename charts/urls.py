from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.charts, name="charts"),
    url(r'^get_data', views.get_data, name='get_data'),
    url(r'^type_data_url', views.type_data_url, name='type_data_url'),
    url(r'^average_feature_progress',
        views.average_feature_progress,
        name='average_feature_progress'),
    url(r'^get_comment_data',
        views.get_comment_data,
        name='get_comment_data'),
    url(r'^get_tickets_by_status',
        views.get_tickets_by_status,
        name="get_tickets_by_status"),
]
