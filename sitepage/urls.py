from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.reg_list, name='reg_list'),
]