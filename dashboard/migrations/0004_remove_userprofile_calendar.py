# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_userprofile_calendar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='calendar',
        ),
    ]
