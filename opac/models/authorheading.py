# -*- coding: utf-8 -*-

from django.db import models


class AUTHORHEADING(models.Model):
    """
    凡例　→　XXXX_(ZZZZ)
    ただし、X,Zどちらもさらにもう一段階半角カンマで区切れる
    """
    # 姓と名の読み書き
    sei_yomi = models.CharField(max_length=255, verbose_name=' 姓 のヨミ', blank=True)
    mei_yomi = models.CharField(max_length=255, verbose_name='名前のヨミ')
    sei_kaki = models.CharField(max_length=255, verbose_name='姓', blank=True)
    mei_kaki = models.CharField(max_length=255, verbose_name='名')

    def __str__(self):
        if self.sei_yomi == "" or self.sei_kaki == "":
            # 姓の部分が空白な場合（著作者が人名でない場合）
            authhead = self.mei_yomi + " " + "(" + self.mei_kaki + ")"
        else:
            # 著作者が人名な場合
            authhead = self.sei_yomi + ", " + self.mei_yomi + " " \
                + "("+ self.sei_kaki + ", " + self.mei_kaki + ")"
        return authhead
