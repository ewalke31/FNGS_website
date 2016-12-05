from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
import os.path as op


class Dataset(models.Model):
	dataset_id = models.CharField(max_length=30)
	collection_site = models.CharField(max_length=40)
	output_url = models.CharField(max_length=200, null=True, blank=True)

	def add_output_url(self, url):
		output_url = models.TextField(url)
			
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
	output_url = models.CharField(max_length=200, null=True, blank=True)
	STC_CHOICES = (
		(None, 'None'),
		('up', 'Bottom Up Acquisition (standard)'),
		('down', 'Top Down Acquisition'),
		("interleaved", 'Interleaved Acquisition')
	)
	slice_timing = models.CharField(max_length=20, choices=STC_CHOICES)
	AN_CHOICES = (
		(1, 'T1w'),
		(2, 'T2w'),
		(3, 'PD')
	)
	an = models.IntegerField(choices=AN_CHOICES, default=1)

	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return ((self.dataset == other.dataset) and (self.sub_id == other.sub_id))
		return False

	def get_id(self):
		return str(op.splitext(op.splitext(op.basename(self.func_scan.name))[0])[0])

	def __ne__(self, other):
		return not self.__eq__(other)

	def add_output_url(self, url):
		output_url = models.TextField(url)

	def __str__(self):
		return str(str(self.dataset) + "_" + str(self.sub_id))
