from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views import generic
from analyze.models import Dataset, Subject
import os
from ndmg.utils import utils as mgu


def index(request):
	datasets = Dataset.objects.all()
	return render(request, 'explore/index.html', {'datasets': datasets})

def dataset(request, dataset_id):
	dataset = get_object_or_404(Dataset, dataset_id=dataset_id)
	return render(request, 'explore/dataset.html', {'dataset': dataset})

def view_subject(request, dataset_id, sub_id):
	dataset = get_object_or_404(Dataset, dataset_id=dataset_id)
	subject = get_object_or_404(Subject, dataset = dataset, sub_id = sub_id)
	if subject.output_url is not None:
		context = {'dataset': dataset, 'subject': subject}
		return render(request, 'explore/subject.html', context)
	else:
		pass
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

def sub_motion_qc(request, dataset_id, sub_id):
	dataset = get_object_or_404(Dataset, dataset_id=dataset_id)
	subject = get_object_or_404(Subject, dataset = dataset, sub_id = sub_id)
	test = mgu().execute_cmd("find " + subject.output_url + " -wholename \"*overall*" + subject.get_id() + "*trans*\"")[0].rstrip('\n')
	print test
	context = {'dataset': dataset,
			   'subject': subject,
			   'trans': mgu().execute_cmd("find " + subject.output_url + " -wholename \"*overall*" + subject.get_id() + "*trans*\"")[0].rstrip('\n'),
			   'rot': mgu().execute_cmd("find " + subject.output_url + " -wholename \"*overall*" + subject.get_id() + "*rot*\"")[0].rstrip('\n'),
			   'disp': mgu().execute_cmd("find " + subject.output_url + " -wholename \"*overall*" + subject.get_id() + "*disp*\"")[0].rstrip('\n'),
			   'mcjitter':mgu().execute_cmd("find " + subject.output_url + " -wholename \"*mc*" + subject.get_id() + "*jitter*\"")[0].rstrip('\n'),
			   'mckde':mgu().execute_cmd("find " + subject.output_url + " -wholename \"*mc*" + subject.get_id() + "*kde*\"")[0].rstrip('\n')}
	return render(request, 'explore/motion.html', context)


def sub_register_qc(request, dataset_id, sub_id):
	dataset = get_object_or_404(Dataset, dataset_id=dataset_id)
	subject = get_object_or_404(Subject, dataset = dataset, sub_id = sub_id)
	context = {'dataset': dataset, 'subject': subject}
	return render(request, 'explore/register.html', context)
	
def sub_timeseries_qc(request, dataset_id, sub_id):
	dataset = get_object_or_404(Dataset, dataset_id=dataset_id)
	subject = get_object_or_404(Subject, dataset = dataset, sub_id = sub_id)
	context = {'dataset': dataset, 'subject': subject}
	return render(request, 'explore/timeseries.html', context)
