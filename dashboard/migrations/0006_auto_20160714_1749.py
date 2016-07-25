# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20160713_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='outlook_connection',
            field=models.OneToOneField(to='dashboard.OutlookConnection', blank=True, default=None, null=True),
        ),
    ]
