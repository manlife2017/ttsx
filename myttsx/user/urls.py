from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^useradd/$', views.useradd),
    url(r'^check_user/$', views.check_user),
    url(r'^check_login/$', views.check_login),
    url(r'^quiter/$', views.quiter),
    url(r'^info/$', views.info),
    url(r'^uorder_(\d+)/$', views.uorder),
    url(r'^usite/$', views.usite),
    url(r'^editinfos/$', views.editinfos),
]
