from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^missing/$', views.missing, name='missing'),
    url(r'^payment/$', views.payment, name='payment'),
]
