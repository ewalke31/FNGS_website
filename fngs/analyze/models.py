from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.core.urlresolvers import reverse_lazy


class Dataset(models.Model):
	dataset_id = models.CharField(max_length=30)
	collection_site = models.CharField(max_length=40)

	def __str__(self):
		return str(self.dataset_id)

	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.dataset_id == other.dataset_id
		return False

	def __ne__(self, other):
		return not self.__eq__(other)


class Subject(models.Model):
	dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
	sub_id = models.CharField(max_length=30)
	struct_scan = models.FileField()
	func_scan = models.FileField()
	
	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return ((self.dataset == other.dataset) and (self.sub_id == other.sub_id))
		return False

	def __ne__(self, other):
		return not self.__eq__(other)


	def __str__(self):
		return str(str(self.dataset) + "_" + str(self.sub_id))
