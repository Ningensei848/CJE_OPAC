# -*- coding: utf-8 -*-

from django.db import models


class RESPONSIBILITY(models.Model):
	"""
	凡例　→　hogehoge，foobar著_;_hugahuga編
	著や編といった貢献区分に、どんな責任表示をもたせるか
	"""
	
	# 貢献区分
	role = models.CharField(max_length=31, verbose_name='貢献区分', blank=True)
	# 責任表示
	people = models.CharField(max_length=255, verbose_name='責任表示')
	
	def __str__(self):
		responsibility = self.role + self.people
		return responsibility
