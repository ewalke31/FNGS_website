from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'explore'

urlpatterns = [
	# /explore/
    url(r'^$', views.index, name='index'),
    # /explore/<dataset_id>/
    url(r'^(?P<dataset_id>[\w\-]+)/$', views.dataset, name='dataset'),
    url(r'dataset/(?P<dataset_id>[\w\-]+)/(?P<sub_id>[\w\-]+)/download/$', views.download_subject, name='subject-download'),
    url(r'dataset/(?P<dataset_id>[\w\-]+)/(?P<sub_id>[\w\-]+)/overall/$', views.sub_overall_qc, name='sub-qc-overall'),
    url(r'dataset/(?P<dataset_id>[\w\-]+)/(?P<sub_id>[\w\-]+)/motion/$', views.sub_motion_qc, name='sub-qc-motion'),
    url(r'dataset/(?P<dataset_id>[\w\-]+)/(?P<sub_id>[\w\-]+)/register/$', views.sub_register_qc, name='sub-qc-register'),
    url(r'dataset/(?P<dataset_id>[\w\-]+)/(?P<sub_id>[\w\-]+)/stats/$', views.sub_stats_qc, name='sub-qc-stats'),
    url(r'dataset/(?P<dataset_id>[\w\-]+)/(?P<sub_id>[\w\-]+)/nuisance/$', views.sub_nuisance_qc, name='sub-qc-nuisance'),
    url(r'dataset/(?P<dataset_id>[\w\-]+)/(?P<sub_id>[\w\-]+)/timeseries/$', views.sub_timeseries_qc, name='sub-qc-timeseries'),
]