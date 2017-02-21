# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20170221_1524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='columns',
            new_name='column',
        ),
    ]
