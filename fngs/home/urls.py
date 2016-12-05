from django.conf.urls import url
from . import views


app_name = 'home'

urlpatterns = [
	# /explore/
    url(r'^$', views.index, name='index'),
    url(r'^$algorithms/', views.algorithms, name='algorithms')
    # /explore/<dataset_id>/
]