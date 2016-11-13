from django.conf.urls import url
from . import views


app_name = 'explore'

urlpatterns = [
	# /explore/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /explore/<dataset_id>/
    url(r'^(?P<dataset_id>[\w\-]+)/$', views.DatasetView.as_view(), name='dataset'),
]