# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='标题', max_length=256)),
                ('slug', models.CharField(verbose_name='网址', db_index=True, max_length=256)),
                ('content', models.TextField(blank=True, verbose_name='内容', default='')),
                ('published', models.BooleanField(verbose_name='正式发布', default=True)),
                ('author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name='作者')),
            ],
            options={
                'verbose_name': '教程',
                'verbose_name_plural': '教程',
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='栏目名称', max_length=256)),
                ('slug', models.CharField(verbose_name='栏目网址', db_index=True, max_length=256)),
                ('intro', models.TextField(verbose_name='栏目简介', default='')),
            ],
            options={
                'verbose_name': '栏目',
                'ordering': ['name'],
                'verbose_name_plural': '栏目',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='columns',
            field=models.ManyToManyField(verbose_name='归属栏目', to='news.Column'),
        ),
    ]
