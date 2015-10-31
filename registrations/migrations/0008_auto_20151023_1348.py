# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0007_auto_20151023_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofiles',
            name='address',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='userprofiles',
            name='age',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='userprofiles',
            name='area',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='userprofiles',
            name='first_name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='userprofiles',
            name='gender',
            field=models.CharField(default=b'None', max_length=2, null=True, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
        migrations.AlterField(
            model_name='userprofiles',
            name='last_name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='userprofiles',
            name='pin',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
