from django.conf.urls import url
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^login$', views.login, name='login'),
    url(r'^resetpassword/$', PasswordResetView.as_view(), name='resetpassword'),
    url(r'^resetpassword/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^resetpassword/done$',
        PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^resetpassword/complete$',
        PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
