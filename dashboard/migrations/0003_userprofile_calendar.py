# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_event_color_event'),
        ('dashboard', '0002_auto_20160606_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='calendar',
            field=models.OneToOneField(to='schedule.Calendar', default=None),
        ),
    ]
