from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.charts),
    url(r'^get_data', views.get_data, name='get_data'),
    url(r'^type_data_url', views.type_data_url, name='type_data_url'),
]