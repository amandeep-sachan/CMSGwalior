# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0002_auto_20151021_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiles',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofiles',
            name='gender',
            field=models.CharField(default=datetime.date(2015, 10, 23), max_length=2, choices=[(b'M', b'Male'), (b'F', b'Female')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofiles',
            name='picture',
            field=models.ImageField(upload_to=b'profile_images/', blank=True),
        ),
    ]
