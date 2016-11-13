from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Dataset


class IndexView(generic.ListView):
	template_name = 'analyze/index.html'
	context_object_name = 'datasets'

	def get_queryset(self):
		return Dataset.objects.all()


class DatasetView(generic.DetailView):
	model = Dataset
	context_object_name = 'dataset'
	template_name = 'analyze/dataset.html'

	def get_object(self):
		return get_object_or_404(Dataset, dataset_id=self.kwargs.get("dataset_id"))


class DatasetCreate(CreateView):
	model = Dataset
	fields = ['dataset_id', 'collection_site']
	context_object_name = 'dataset'

	def get_object(self):
		return get_object_or_404(Dataset, dataset_id=self.kwargs.get("dataset_id"))

class DatasetUpdate(UpdateView):
	model = Dataset
	fields = ['dataset_id', 'collection_site']
	context_object_name = 'dataset'	

	def get_object(self):
		return get_object_or_404(Dataset, dataset_id=self.kwargs.get("dataset_id"))

class DatasetDelete(DeleteView):
	model = Dataset
	success_url = reverse_lazy('analyze:index')

	def get_object(self):
		return get_object_or_404(Dataset, dataset_id=self.kwargs.get("dataset_id"))