# -*- coding: utf-8 -*-

from django.db import models


class PUB(models.Model):
	"""
	凡例　→　出版地_:_出版者,_出版年.出版月
	"""
	# 出版地
	publishedArea = models.CharField(max_length=31, verbose_name='出版地')
	# 出版者
	publisher = models.CharField(max_length=255, verbose_name='出版者')
	# 出版年
	publishedYear = models.IntegerField(verbose_name='出版年')
	# 出版月
	publishedMonth = models.IntegerField(verbose_name='出版月')
	
	def __str__(self):
		pub = self.publishedArea + " : " + self.publisher + "," \
		      + str(self.publishedYear) + "." + str(self.publishedMonth)
		return pub
