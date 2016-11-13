from django.http import HttpResponse
from .models import Dataset

def index(request):
	all_datasets = Dataset.objects.all()
	html = ''
	for dataset in all_datasets:
		url = '/explore/' + str(dataset.dataset_id) + '/'
		html += '<a href="' + url + '"/a>' + dataset.dataset_id + '<br>'

	return HttpResponse(html)

def detail(request, dataset_id):
	return HttpResponse("<h1>Details for Dataset Id: " + str(dataset_id) + "</h1>")
