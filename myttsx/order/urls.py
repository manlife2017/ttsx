from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^place_order/$', views.place_order),
    url(r'^create_order/$', views.create_order),
]
