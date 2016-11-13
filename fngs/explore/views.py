from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views import generic
from analyze.models import Dataset

class IndexView(generic.ListView):
	template_name = 'explore/index.html'
	context_object_name = 'datasets'

	def get_queryset(self):
		return Dataset.objects.all()


class DatasetView(generic.DetailView):
	model = Dataset
	context_object_name = 'dataset'

	template_name = 'explore/dataset.html'

	def get_object(self):
		return get_object_or_404(Dataset, dataset_id=self.kwargs.get("dataset_id"))