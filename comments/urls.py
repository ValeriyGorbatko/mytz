from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.TreeListView.as_view(), name='tree_list')
]
