from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^missing/$', views.missing, name='missing'),
    url(r'^payment/$', views.payment, name='payment'),
    url(r'^demo/$', views.demo, name='demo'),
    url(r'^demoresult/$', views.update, name='demoresult'),
    url(r'^dues/$', views.dueren, name='dueren'),
    url(r'^data/$', views.dues, name='dues'),
]
