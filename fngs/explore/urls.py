from django.conf.urls import url
from . import views


app_name = 'explore'

urlpatterns = [
	# /explore/
    url(r'^$', views.index, name='index'),
    # /explore/<dataset_id>/
    url(r'^(?P<dataset_id>[\w\-]+)/$', views.dataset, name='dataset'),
    url(r'dataset/(?P<dataset_id>[\w\-]+)/(?P<sub_id>[\w\-]+)/view/$', views.view_subject, name='subject-view'),
    url(r'dataset/(?P<dataset_id>[\w\-]+)/(?P<sub_id>[\w\-]+)/download/$', views.download_subject, name='subject-download'),
]