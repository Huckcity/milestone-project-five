from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.view_cart, name='cart'),
    url(r'^add/(?P<featureid>\d+)/$', views.addtocart, name='addtocart'),
    # url(r'^remove/(?P<featureid>\d+)/$', views.removefromcart, name='removefromcart'),
    url(r'^checkout$', views.checkout, name='checkout'),
    url(r'^charge$', views.charge, name='charge'),
]
