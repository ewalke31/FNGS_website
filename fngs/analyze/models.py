from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.core.urlresolvers import reverse_lazy


class Dataset(models.Model):
	dataset_id = models.CharField(max_length=30)
	collection_site = models.CharField(max_length=40)

	def get_absolute_url(self):
		return reverse('analyze:dataset', kwargs={'dataset_id': self.dataset_id})

	def __str__(self):
		return str(self.dataset_id)

class Subject(models.Model):
	dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
	sub_id = models.CharField(max_length=30)
	struct_scan = models.FileField()
	func_scan = models.FileField()

	def get_absolute_url(self):
		return reverse_lazy('analyze:dataset', kwargs={'dataset_id': self.dataset.dataset_id})

	def __str__(self):
		return str(str(self.dataset) + "_" + str(self.sub_id))
