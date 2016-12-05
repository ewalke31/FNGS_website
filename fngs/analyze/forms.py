from django import forms
from django.contrib.auth.models import User
from .models import Dataset, Subject
from django.utils.translation import ugettext_lazy as _


class DatasetForm(forms.ModelForm):
    class Meta:
        model = Dataset
        fields = ['dataset_id', 'collection_site']
        labels={
        	'dataset': _('Dataset'),
        	'collection_site':_('Collection Site')
        }
        help_texts={
        	'dataset': _('The name of the dataset this subject is a part of.'),
        	'collection_site':_('The location the dataset was collected.')
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['dataset', 'sub_id', 'func_scan', 'struct_scan','an', 'slice_timing']
        labels={
        	'dataset': _('Dataset'),
        	'sub_id': _('Subject ID'),
        	'func_scan':_('Functional Scan'),
        	'struct_scan':_('Structural Scan'),
        	'an':_('Structural scan type'),
        	'slice_timing':_('Slice Timing Method')
        }
        help_texts={
        	'dataset': _('The name of the dataset this subject is a part of.'),
        	'sub_id': _('A unique identifier for the subject.'),
        	'func_scan':_('the fMRI of this subject.'),
        	'struct_scan':_('the structural MRI of this subject.'),
        	'an':_('The Type of structural scan.'),
        	'slice_timing':_('The method in which slices were acquired.')
        }
