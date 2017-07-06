from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list_(\d+)_(\d+)_(\d+)/$', views.list),
    url(r'^goodinfo_(\d+)/$', views.goodinfo)
]
