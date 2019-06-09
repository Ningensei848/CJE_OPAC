# -*- coding: utf-8 -*-
from django.db import models

# #################################################################################################################


class BIBLIO(models.Model):
    """
    DB：NBC，ISBN，TR，ED, PUB, PHYS, SERIES, NOTE,
        TITLEHEADING, AUTHORHEADING, HOLDINGSRECORD, HOLDINGPHYS, HOLDINGLOC

    example:
    NBC: JP20625031
    ISBN: ISBN4-86107-010-4
    TR: 私達の日本人論 : 故郷は遠きにありて思うもの 愛知教育大学名誉教授旧姓、板橋美智子の永眠 / 加藤方寅編著
    ED: 新改訂版
    PUB: 広島 : ガリバープロダクツ, 2004.6
    PHYS: 344p ; 19cm
    SERIES: ガリバーbooks
    NOTE: hogehoge
    TITLEHEADING: ワタシタチ ノ ニホンジン ロン
    TITLEHEADING: ガリバー books
    AUTHORHEADING: カトウ, ミチノブ (加藤, 方寅)
    HOLDINGSRECORD: JP20625031-01
    HOLDINGPHYS: hogehoge
    HOLDINGLOC: NDL EC225-H86
    *
    """

    # opacの要件
    nbc = models.CharField(
        max_length=31,
        verbose_name='NBC(全国書誌番号)',
        primary_key=True
    )  # JP+8桁？
    # ISBN # 複数の場合あり?
    # isbn = models.ForeignKey(
    #     'ISBN',
    #     verbose_name='ISBN',
    #     on_delete=models.PROTECT,
    #     # default=ISBN.objects.get(prefix=000, group=0, publisher=0000, title=0000, check=0),
    #     blank=True
    # )
    # ISBN (暫定)
    isbn = models.CharField(
        max_length=63,
        verbose_name='ISBN',
    )
    # 責任者表示
    # 主題
    title = models.CharField(
        max_length=255,
        verbose_name='主題'
    )
    # 副題
    sub_title = models.CharField(
        max_length=255,
        verbose_name='副題',
        blank=True
    )
    # 責任表示
    responsibility = models.CharField(
        max_length=255,
        verbose_name='責任者',
        blank=True
    )
    # 版表示
    ed = models.CharField(
        max_length=31,
        verbose_name='版表示',
        blank=True,
    )
    # 出版地
    publishedArea = models.CharField(
        max_length=31,
        verbose_name='出版地',
        blank=True,
    )
    # 出版者
    publisher = models.CharField(
        max_length=255,
        verbose_name='出版者',
        blank=True,
    )
    # 出版年
    publishedYear = models.IntegerField(
        verbose_name='出版年',
        blank=True,
    )
    # 出版月
    publishedMonth = models.IntegerField(
        verbose_name='出版月',
        blank=True,
    )
    # 物理的単位PHYS =>  (ページ数, 寸法)
    # ページ数
    page = models.IntegerField(
        verbose_name='ページ数',
    )
    # 寸法
    size = models.CharField(
        max_length=31,
        verbose_name='寸法',
    )
    # シリーズ表示
    series = models.CharField(
        max_length=255,
        verbose_name='シリーズ',
        blank=True
    )
    # 自由記述
    note = models.TextField(
        verbose_name='補足情報',
        blank=True,
    )
    # タイトルの読み（複数パターンある可能性）
    titleheading = models.CharField(
        max_length=255,
        verbose_name='題名のヨミ',
    )
    # 著作者の読み（複数パターンある可能性）
    authorheading = models.CharField(
        max_length=255,
        verbose_name='著作者のヨミ',
        # default=AUTHORHEADING.objects.get(sei_yomi="", mei_yomi="データが見つかりません。", sei_kaki="", mei_kaki="すぐに編集してください")
    )
    # 複本の扱い
    holdingsrecord = models.CharField(
        max_length=31,
        verbose_name='複本記号',
        blank=True,
    )  # 一意
    # なぞの欄
    holdingphys = models.CharField(
        max_length=255,
        verbose_name='所在地詳細',
        blank=True,
    )
    # 所在記号
    holdingloc = models.CharField(
        max_length=31,
        verbose_name='所在記号',
        blank=True,
    )  # 一意
    # # 作成日時
    # datetime = models.DateTimeField(default=now, verbose_name='作成日時')

    def __str__(self):
        result = str(self.nbc)
        return result
# ###################################################################################################################

# CREATE TABLE IF NOT EXISTS "opac_biblio" ("nbc" varchar(31) NOT NULL PRIMARY KEY, "isbn" varchar(63) NOT NULL, "title" varchar(255) NOT NULL, "sub_title" varchar(255) NOT NULL, "responsibility" varchar(255) NOT NULL, "ed" varchar(31) NOT NULL, "publishedArea" varchar(31) NOT NULL, "publisher" varchar(255) NOT NULL, "publishedYear" integer NOT NULL, "publishedMonth" integer NOT NULL, "page" integer NOT NULL, "size" varchar(31) NOT NULL, "series" varchar(255) NOT NULL, "note" text NOT NULL, "titleheading" varchar(255) NOT NULL, "authorheading" varchar(255) NOT NULL, "holdingsrecord" varchar(31) NOT NULL, "holdingphys" varchar(255) NOT NULL, "holdingloc" varchar(31) NOT NULL);
