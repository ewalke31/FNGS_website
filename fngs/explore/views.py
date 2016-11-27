from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views import generic
from analyze.models import Dataset, Subject
import os

def index(request):
	datasets = Dataset.objects.all()
	return render(request, 'explore/index.html', {'datasets': datasets})

def dataset(request, dataset_id):
	dataset = get_object_or_404(Dataset, dataset_id=dataset_id)
	return render(request, 'explore/dataset.html', {'dataset': dataset})

def view_subject(request, dataset_id, sub_id):
	dataset = get_object_or_404(Dataset, dataset_id=dataset_id)
	return render(request, 'explore/dataset.html', {'dataset': dataset})

def download_subject(request, dataset_id, sub_id):
	dataset = get_object_or_404(Dataset, dataset_id=dataset_id)
	subject = get_object_or_404(Subject, dataset = dataset, sub_id = sub_id)
	## TODO: handle this better here; don't just return the same page
	if subject.output_url is not None:
		file_path = subject.output_url + ".zip"
		if os.path.exists(file_path):
			with open(file_path, 'rb') as fh:
				response = HttpResponse(fh.read(), content_type='application/zip')
				response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
				return response
		else:
			raise Http404
	return render(request, 'explore/dataset.html', {'dataset': dataset})
