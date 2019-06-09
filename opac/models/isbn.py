# -*- coding: utf-8 -*-
from django.db import models


class ISBN(models.Model):
	"""
	[ISBN - Wikipedia](https://ja.wikipedia.org/wiki/ISBN)
	1980年より前　ISBNなし（？）
	旧規格: ISBN● - AAAA - BBBB - C
	新規格: ISBNnnn - ● - AAAA - BBBB - C　
	※なお、旧規格には978を挿入し、13ケタとして扱う事になっている
	※●、A、Bの各部分の割り当て桁数は決まっておらず、
	　合計で9桁（必ず1桁のC部分を入れると10桁）となる範囲内で、
	　それぞれの部分は増減する。
	"""
	# 接頭記号nnn
	# prefix = models.IntegerField(default=978)  # 978 or 979 のいずれかのみ
	# グループ記号●
	group = models.IntegerField()  # 主に1 or 2桁（3ケタ以上となるグループもある）
	# 出版者記号AAAA
	publisher = models.IntegerField()
	# 書名記号BBBB
	title = models.IntegerField()
	# チェックディジットC (1桁)
	checkdigit = models.CharField(
		max_length=1
	)  # 0 - 9が使用される。（Xが含まれていた場合の例外処理も考える必要がある）
	
	def __str__(self):
		# ISBN-13
		# isbn = str(self.prefix) + "-" + str(self.group) + "-" \
		#        + str(self.publisher) + "-" + str(self.title) + "-" \
		#        + str(self.checkdigit)

		# ISBN-10
		isbn = str(self.group) + "-" + str(self.publisher) + "-" \
			   + str(self.title) + "-" + str(self.checkdigit)
		return isbn
