# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_remove_userprofile_calendar'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutlookConnection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('user_email', models.CharField(max_length=254)),
                ('access_token', models.TextField()),
                ('refresh_token', models.TextField()),
                ('outlook_resource_id', models.URLField()),
                ('outlook_api_endpoint', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='connected_with_outlook',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='outlook_connection',
            field=models.OneToOneField(to='dashboard.OutlookConnection', default=None),
        ),
    ]
