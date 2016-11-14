from django import forms
from django.contrib.auth.models import User
from .models import Dataset, Subject


class DatasetForm(forms.ModelForm):
    class Meta:
        model = Dataset
        fields = ['dataset_id', 'collection_site']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['dataset', 'sub_id', 'func_scan', 'struct_scan']
