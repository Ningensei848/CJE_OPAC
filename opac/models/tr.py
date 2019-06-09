# -*- coding: utf-8 -*-

from django.db import models


class TR(models.Model):
	"""
	凡例　→　主題_:_副題_/_責任者+著
	副題はないこともある
	責任者表示が無いこともある
	責任者を区切るときは全角カンマ
	"""
	
	# 主題
	title = models.CharField(max_length=255, verbose_name='主題')
	# 副題
	sub_title = models.CharField(max_length=255, verbose_name='副題', blank=True)
	# 責任表示
	responsibility = models.CharField(max_length=255, verbose_name='責任者', blank=True)
	# responsibility = models.ForeignKey('', on_delete=models.PROTECT)
	# # 貢献区分
	# contribution = models.CharField(max_length=31, verbose_name='区分', blank=True)
	
	# もっと工夫するのなら、著者部分だけ切り出したい
	
	def __str__(self):
		if self.responsibility == "" and self.sub_title=="": # 責任表示がない場合
			tr = self.title
		elif self.sub_title == "": # 副題がない場合
			tr = self.title + " / " + self.responsibility
		else:
			tr = self.title + " : " + self.sub_title + " / " + self.responsibility
		return tr
