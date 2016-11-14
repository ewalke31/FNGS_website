from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Dataset, Subject
from .forms import DatasetForm, SubjectForm
from ndmg.scripts.fngs_pipeline import fngs_pipeline

BRAIN_FILE_TYPES = ['nii', 'nii.gz']

def index(request):
	datasets = Dataset.objects.all()
	return render(request, 'analyze/index.html', {'datasets': datasets})


def dataset(request, dataset_id):
	dataset = get_object_or_404(Dataset, dataset_id=dataset_id)
	return render(request, 'analyze/dataset.html', {'dataset': dataset})

def create_dataset(request):
	form = DatasetForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		for dataset in Dataset.objects.all():
			if dataset.dataset_id == form.cleaned_data.get("dataset_id"):
				context = {
					'dataset': dataset,
					'error_message': 'You already added that dataset.',
				}
				return render(request, 'analyze/create_dataset.html', context)
		dataset = form.save(commit=False)
		dataset.save()
		return render(request, 'analyze/dataset.html', {'dataset': dataset})
	context = {
		"form": form,
	}
	return render(request, 'analyze/create_dataset.html', context)


def create_subject(request, dataset_id):
	form = SubjectForm(request.POST or None, request.FILES or None)
	dataset = get_object_or_404(Dataset, dataset_id=dataset_id)
	if form.is_valid():
		dataset_subs = dataset.subject_set.all()
		for sub in dataset_subs:
			if sub.sub_id == form.cleaned_data.get("sub_id"):
				context = {
					'dataset': dataset,
					'form': form,
					'error_message': 'You already added that subject',
				}
				return render(request, 'analyze/create_subject.html', context)
		subject = form.save(commit=False)
		subject.dataset = dataset
		subject.struct_scan = request.FILES['struct_scan']
		file_type = subject.struct_scan.url.split('.', 1)[-1]
		file_type = file_type.lower()
		print(file_type)
		if file_type not in BRAIN_FILE_TYPES:
			context = {
				'album': dataset,
				'form': form,
				'error_message': 'Brain File must be .nii or .nii.gz',
			}
			return render(request, 'analyze/create_subject.html', context)
		subject.func_scan = request.FILES['func_scan']
		file_type = subject.func_scan.url.split('.', 1)[-1]
		file_type = file_type.lower()
		if file_type not in BRAIN_FILE_TYPES:
			context = {
				'dataset': dataset,
				'form': form,
				'error_message': 'Brain File must be .nii or .nii.gz',
			}
			return render(request, 'analyze/create_subject.html', context)
		subject.save()
		return render(request, 'analyze/dataset.html', {'dataset': dataset})
	context = {
		"form": form,
	}
	return render(request, 'analyze/create_subject.html', context)


def analyze_subject(request, dataset_id, sub_id):
	dataset = get_object_or_404(Dataset, dataset_id=dataset_id)
	subject = get_object_or_404(Subject, dataset=dataset, sub_id=sub_id)
	my_home = '/home/eric/demo_atlases/'
	print(subject.func_scan.url)
	fngs_pipeline(subject.func_scan.url, subject.struct_scan.url, 
		my_home + 'atlas/MNI152_T1_2mm.nii.gz', my_home + 'atlas/MNI152_T1_2mm_brain.nii.gz',
		my_home + 'mask/MNI152_T1_2mm_brain_mask.nii.gz', [my_home + 'label/desikan_2mm.nii.gz'],
		stc=None, outdir='/home/eric/testruns')
	return render(request, 'analyze/dataset.html', {'dataset':dataset})

def get_results(request, dataset_id, sub_id):
	pass

def delete_dataset(request, dataset_id):
	dataset = get_object_or_404(Dataset, dataset_id=dataset_id)
	dataset.delete()
	datasets = Dataset.objects.all()
	return render(request, 'analyze/index.html', {'datasets': datasets})


def delete_subject(request, dataset_id, sub_id):
	dataset = get_object_or_404(Dataset, dataset_id=dataset_id)
	subject = get_object_or_404(Subject, dataset=dataset, sub_id=sub_id)
	subject.delete()
	datasets = Dataset.objects.all()
	return render(request, 'analyze/dataset.html', {'dataset': dataset})
