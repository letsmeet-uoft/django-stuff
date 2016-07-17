# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20160714_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='connected_with_outlook',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='outlook_connection',
        ),
        migrations.DeleteModel(
            name='OutlookConnection',
        ),
    ]
