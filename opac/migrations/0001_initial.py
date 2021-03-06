# Generated by Django 2.2.1 on 2019-06-11 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BIBLIO',
            fields=[
                ('nbc', models.CharField(max_length=31, primary_key=True, serialize=False, verbose_name='NBC(全国書誌番号)')),
                ('isbn', models.CharField(max_length=63, verbose_name='ISBN')),
                ('title', models.CharField(max_length=255, verbose_name='主題')),
                ('sub_title', models.CharField(blank=True, max_length=255, verbose_name='副題')),
                ('responsibility', models.CharField(blank=True, max_length=255, verbose_name='責任者')),
                ('ed', models.CharField(blank=True, max_length=31, verbose_name='版表示')),
                ('publishedArea', models.CharField(blank=True, max_length=31, verbose_name='出版地')),
                ('publisher', models.CharField(blank=True, max_length=255, verbose_name='出版者')),
                ('publishedYear', models.IntegerField(blank=True, verbose_name='出版年')),
                ('publishedMonth', models.IntegerField(blank=True, verbose_name='出版月')),
                ('page', models.IntegerField(verbose_name='ページ数')),
                ('size', models.CharField(max_length=31, verbose_name='寸法')),
                ('series', models.CharField(blank=True, max_length=255, verbose_name='シリーズ')),
                ('note', models.TextField(blank=True, verbose_name='補足情報')),
                ('titleheading', models.CharField(max_length=255, verbose_name='題名のヨミ')),
                ('authorheading', models.CharField(max_length=255, verbose_name='著作者のヨミ')),
                ('holdingsrecord', models.CharField(blank=True, max_length=31, verbose_name='複本記号')),
                ('holdingphys', models.CharField(blank=True, max_length=255, verbose_name='所在地詳細')),
                ('holdingloc', models.CharField(blank=True, max_length=31, verbose_name='所在記号')),
            ],
        ),
    ]
