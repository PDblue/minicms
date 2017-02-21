# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 2, 21, 7, 24, 49, 280251, tzinfo=utc), verbose_name='发表时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(null=True, auto_now=True, verbose_name='更新时间'),
        ),
    ]
