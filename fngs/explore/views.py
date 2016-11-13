from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from analyze.models import Dataset


def index(request):
	datasets = Dataset.objects.all()
	context = {
		'datasets': datasets,
	}
	return render(request, 'explore/index.html', context)

def dataset(request, dataset_id):
	dataset = get_object_or_404(Dataset, dataset_id = dataset_id)

	return render(request, 'explore/dataset.html', {'dataset': dataset})
	