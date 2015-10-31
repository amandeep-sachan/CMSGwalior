# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofiles',
            name='mobile',
            field=models.BigIntegerField(unique=True, null=True),
        ),
    ]
