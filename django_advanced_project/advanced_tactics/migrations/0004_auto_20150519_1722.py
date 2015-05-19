# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('advanced_tactics', '0003_auto_20150519_1707'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(default=b'San Francisco', max_length=60),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 19, 17, 22, 57, 798770)),
        ),
    ]
