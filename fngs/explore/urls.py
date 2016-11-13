from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^^(?P<dataset_id>[\w\-]+)/$', views.detail, name='detail'),
]
