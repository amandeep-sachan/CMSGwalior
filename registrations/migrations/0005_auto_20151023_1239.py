# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0004_auto_20151023_1218'),
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
            field=models.CharField(default=1, max_length=2, choices=[(b'M', b'Male'), (b'F', b'Female')]),
            preserve_default=False,
        ),
    ]
