from django.conf.urls import url
from . import views


app_name = 'analyze'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<dataset_id>[\w\-]+)/$', views.DatasetView.as_view(), name='dataset'),
    url(r'dataset/add/$', views.DatasetCreate.as_view(), name='dataset-add'),
    url(r'dataset/(?P<dataset_id>[\w\-]+)/$', views.DatasetUpdate.as_view(), name='dataset-update'),
    url(r'dataset/(?P<dataset_id>[\w\-]+)/delete/$', views.DatasetDelete.as_view(), name='dataset-delete'),
    #url(r'dataset/(?P<dataset_id>[\w\-]+)/(?P<sub_id>[\w\-]+)/analyze/$', views.AnalyzeSubject.as_view(), name='subject-add'),
    url(r'dataset/(?P<dataset_id>[\w\-]+)/subject/add/$', views.SubjectCreate.as_view(), name='subject-add'),
    url(r'dataset/(?P<dataset_id>[\w\-]+)/(?P<sub_id>[\w\-]+)/delete/$', views.SubjectDelete.as_view(), name='subject-delete'),
]
