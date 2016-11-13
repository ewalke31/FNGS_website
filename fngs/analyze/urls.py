from django.conf.urls import url
from . import views


app_name = 'analyze'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<dataset_id>[\w\-]+)/$', views.DatasetView.as_view(), name='dataset'),
    url(r'dataset/add/$', views.DatasetCreate.as_view(), name='dataset-add'),
    url(r'dataset/(?P<dataset_id>[\w\-]+)/$', views.DatasetUpdate.as_view(), name='dataset-update'),
    url(r'dataset/(?P<dataset_id>[\w\-]+)/delete/$', views.DatasetDelete.as_view(), name='dataset-delete'),
]
