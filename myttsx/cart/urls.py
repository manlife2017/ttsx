from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^mycart/$', views.mycart),
    url(r'^goodtocart/$', views.goodtocart),
    url(r'^ed_count/$', views.ed_count),
    url(r'^del_good/$', views.del_good),
]
