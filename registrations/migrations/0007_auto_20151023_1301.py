# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0006_auto_20151023_1243'),
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
            field=models.CharField(default=b'None', max_length=2, choices=[(b'M', b'Male'), (b'F', b'Female')]),
            preserve_default=True,
        ),
    ]
